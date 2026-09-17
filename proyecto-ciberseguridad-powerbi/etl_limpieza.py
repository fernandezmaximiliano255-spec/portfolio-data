from pathlib import Path
import pandas as pd

BASE = Path(__file__).parent
RAW = BASE / "data" / "incidentes_raw.csv"
OUT = BASE / "output"

def normalizar_texto(s):
    return s.astype("string").str.strip().str.lower().str.replace(r"\s+", " ", regex=True)

def main():
    OUT.mkdir(exist_ok=True)
    df = pd.read_csv(RAW, dtype="string")
    texto = ["cliente", "categoria", "severidad", "estado", "analista", "canal", "descripcion"]
    for col in texto:
        df[col] = normalizar_texto(df[col])

    # Homogeneizar nombres que aparecen con acento o variantes de escritura.
    df["cliente"] = df["cliente"].replace({"banco río": "banco rio"})
    df["categoria"] = df["categoria"].replace({"acceso no autorizado": "acceso no autorizado", "exfiltración": "exfiltracion"})
    df["severidad"] = df["severidad"].replace({"critica": "crítica", "alta": "alta", "media": "media", "baja": "baja"})
    df["estado"] = df["estado"].replace({"en análisis": "en analisis", "en análisis": "en analisis"})

    for col in ["fecha_deteccion", "fecha_respuesta", "fecha_cierre"]:
        df[col] = pd.to_datetime(df[col], dayfirst=True, errors="coerce")
    df["sla_respuesta_horas"] = pd.to_numeric(df["sla_respuesta_horas"], errors="coerce")

    # El ID identifica el incidente; conservamos la primera fila del duplicado.
    df = df.drop_duplicates(subset=["id_incidente"], keep="first").copy()
    df["tiempo_respuesta_horas"] = (df["fecha_respuesta"] - df["fecha_deteccion"]).dt.total_seconds() / 3600
    df["tiempo_resolucion_horas"] = (df["fecha_cierre"] - df["fecha_deteccion"]).dt.total_seconds() / 3600
    df["cumple_sla"] = df["tiempo_respuesta_horas"].le(df["sla_respuesta_horas"])
    df["cumple_sla"] = df["cumple_sla"].fillna(False)
    df["mes"] = df["fecha_deteccion"].dt.to_period("M").astype("string")
    df["fecha_deteccion"] = df["fecha_deteccion"].dt.strftime("%Y-%m-%d %H:%M")
    for col in ["fecha_respuesta", "fecha_cierre"]:
        df[col] = df[col].dt.strftime("%Y-%m-%d %H:%M")
    df.to_csv(OUT / "incidentes_limpios.csv", index=False, encoding="utf-8-sig")

    kpis = (df.assign(cumple_sla_num=df["cumple_sla"].astype(int))
              .groupby("mes", dropna=False)
              .agg(incidentes=("id_incidente", "count"),
                   incidentes_criticos=("severidad", lambda s: (s == "crítica").sum()),
                   sla_cumplido_pct=("cumple_sla_num", "mean"),
                   respuesta_media_horas=("tiempo_respuesta_horas", "mean"),
                   resolucion_media_horas=("tiempo_resolucion_horas", "mean"))
              .reset_index())
    kpis["sla_cumplido_pct"] = (kpis["sla_cumplido_pct"] * 100).round(1)
    kpis.round(1).to_csv(OUT / "kpis_por_mes.csv", index=False, encoding="utf-8-sig")

    diccionario = pd.DataFrame([
        ["id_incidente", "Identificador único del incidente"], ["cliente", "Organización afectada"],
        ["categoria", "Tipo de amenaza o hallazgo"], ["severidad", "Nivel de impacto"],
        ["estado", "Estado operativo del caso"], ["analista", "Analista asignado"],
        ["tiempo_respuesta_horas", "Horas entre detección y primera respuesta"],
        ["tiempo_resolucion_horas", "Horas entre detección y cierre"],
        ["cumple_sla", "Primera respuesta dentro del SLA"],
    ], columns=["campo", "definicion"])
    diccionario.to_csv(OUT / "catalogo_campos.csv", index=False, encoding="utf-8-sig")
    print(f"Filas originales:  {30 + 1}")
    print(f"Filas finales:     {len(df)}")
    print(f"Duplicados quitados: {31 - len(df)}")
    print(f"Archivos generados en: {OUT}")

if __name__ == "__main__":
    main()
