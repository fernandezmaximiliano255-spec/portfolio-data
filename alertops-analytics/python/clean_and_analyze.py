from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
RAW_FILE = ROOT / "data" / "alerts_raw.csv"
CLEAN_FILE = ROOT / "data" / "alerts_clean.csv"


def load_and_clean() -> pd.DataFrame:
    df = pd.read_csv(RAW_FILE, parse_dates=["alert_date"])

    numeric_columns = ["amount_usd", "risk_score", "resolution_hours"]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df["month"] = df["alert_date"].dt.to_period("M").astype(str)
    df["is_open"] = df["status"].isin(["in_review", "escalated"])
    df["is_false_positive"] = df["resolution_type"].eq("false_positive")
    df["sla_hours"] = df["severity"].map(
        {"critical": 8, "high": 12, "medium": 24, "low": 48}
    )
    df["sla_breached"] = df["resolution_hours"].gt(df["sla_hours"])
    df["priority"] = pd.cut(
        df["risk_score"],
        bins=[-1, 49, 74, 89, 100],
        labels=["low", "medium", "high", "critical"],
    ).astype(str)

    return df


def print_summary(df: pd.DataFrame) -> None:
    total = len(df)
    open_cases = int(df["is_open"].sum())
    resolved = df["resolution_type"].notna().sum()
    false_positive_rate = df["is_false_positive"].mean() * 100
    resolved_sla = df.loc[df["resolution_hours"].notna(), "sla_breached"].mean()
    sla_compliance = (1 - resolved_sla) * 100

    print("AlertOps Analytics - resumen")
    print(f"Alertas totales: {total}")
    print(f"Casos abiertos o escalados: {open_cases}")
    print(f"Casos resueltos: {resolved}")
    print(f"Tasa de falsos positivos: {false_positive_rate:.1f}%")
    print(f"Cumplimiento de SLA: {sla_compliance:.1f}%")
    print("\nAlertas por regla:")
    print(df["rule_name"].value_counts().to_string())


if __name__ == "__main__":
    alerts = load_and_clean()
    alerts.to_csv(CLEAN_FILE, index=False)
    print_summary(alerts)
