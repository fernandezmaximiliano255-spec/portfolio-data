import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


ARCHIVO = "brava_cafe_campania.xlsx"


def main():
    df = pd.read_excel(ARCHIVO, sheet_name="Dataset_Modelo")

    print("Primeras filas:")
    print(df.head())
    print("\nDimensiones:", df.shape)
    print("\nInformación:")
    print(df.info())

    print("\nPromedios según respuesta:")
    print(df.groupby("Respondio")[[
        "PedidosPrevios",
        "GastoPromedio",
        "DiasDesdeUltimaCompra",
        "PedidosDeOrigen",
        "UsoCuponPrevio",
    ]].mean())

    respuesta_canal = df.groupby("Canal")["Respondio"].agg(
        TasaRespuesta="mean",
        Clientes="count",
    )
    respuesta_canal["TasaRespuesta"] *= 100
    print("\nTasa de respuesta por canal:")
    print(respuesta_canal)

    respuesta_provincia = df.groupby("Provincia")["Respondio"].agg(
        TasaRespuesta="mean",
        Clientes="count",
    )
    respuesta_provincia["TasaRespuesta"] *= 100
    print("\nTasa de respuesta por provincia:")
    print(respuesta_provincia.sort_values("TasaRespuesta", ascending=False))

    X = df.drop(columns=["Respondio", "ClienteID"])
    y = df["Respondio"]

    X_codificado = pd.get_dummies(
        X,
        columns=["Canal", "Provincia"],
        dtype=int,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X_codificado,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    modelo = Pipeline([
        ("escalado", StandardScaler()),
        ("regresion_logistica", LogisticRegression(max_iter=1000)),
    ])
    modelo.fit(X_train, y_train)

    predicciones = modelo.predict(X_test)
    exactitud = accuracy_score(y_test, predicciones)

    print("\nExactitud del modelo:")
    print(f"{exactitud:.2%}")
    print("\nMatriz de confusión:")
    print(confusion_matrix(y_test, predicciones))
    print("\nReporte de clasificación:")
    print(classification_report(y_test, predicciones))

    coeficientes = modelo.named_steps["regresion_logistica"].coef_[0]
    importancia = pd.DataFrame({
        "Variable": X_codificado.columns,
        "Coeficiente": coeficientes,
    }).sort_values("Coeficiente", ascending=False)

    print("\nImportancia de las variables:")
    print(importancia.to_string(index=False))

    respuesta_canal["TasaRespuesta"].sort_values().plot(
        kind="bar",
        color="#7B3F2A",
        title="Tasa de respuesta por canal",
        ylabel="Tasa de respuesta (%)",
        xlabel="Canal",
    )
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
