# Brava Café - Predicción de respuesta a una campaña

## Resumen ejecutivo

Este proyecto analiza una campaña comercial de **Brava Café de Especialidad**, una empresa ficticia argentina que vende café y accesorios a través de una tienda online.

La campaña se diseñó para promocionar **Colombia 250 g con un descuento del 15%**. El objetivo fue identificar qué clientes tenían mayor probabilidad de comprar después de recibir la promoción y utilizar esa información para orientar mejor los contactos comerciales.

El proyecto combina un modelo de datos relacional, análisis exploratorio en Python y un primer modelo de Machine Learning basado en regresión logística.

## Objetivo de negocio

Responder la siguiente pregunta:

> ¿Qué clientes tienen mayor probabilidad de responder a una campaña de promoción de café de origen?

La variable objetivo es `Respondio`:

- `1`: el cliente compró después de recibir la campaña.
- `0`: el cliente no compró dentro de la ventana analizada.

## Estructura del archivo Excel

El archivo `brava_cafe_campania.xlsx` contiene las tablas del negocio y el dataset preparado para el modelo:

- `Clientes`: información básica, provincia, ciudad y canal de alta.
- `Pedidos`: compras realizadas, fecha, cupón y costo de envío.
- `PedidoDetalle`: productos, cantidades, precios y costos unitarios.
- `Productos`: catálogo, categorías, precios y costos.
- `Categorias`: clasificación de productos.
- `Campanias`: clientes contactados, canal, promoción y resultado.
- `Dataset_Modelo`: una fila por cliente contactado y las variables utilizadas para predecir la respuesta.

## Herramientas utilizadas

- Python.
- pandas para carga, limpieza y análisis de datos.
- matplotlib para visualización.
- scikit-learn para la división de datos, regresión logística y métricas.
- Excel como fuente de datos y documentación del modelo de negocio.

## Proceso de análisis

1. Se cargó la hoja `Dataset_Modelo` con pandas.
2. Se revisaron dimensiones, tipos de datos y valores faltantes.
3. Se compararon los promedios de clientes que respondieron y no respondieron.
4. Se analizaron las tasas de respuesta por canal, provincia y combinación de provincia y canal.
5. Se separaron las variables predictoras de la variable objetivo.
6. Se codificaron las variables categóricas mediante one-hot encoding.
7. Se dividieron los datos en entrenamiento y prueba, usando 80% y 20% respectivamente.
8. Se entrenó una regresión logística.
9. Se evaluó el modelo con exactitud, matriz de confusión, precisión, recall y F1-score.

## Hallazgos del análisis exploratorio

- La tasa general de respuesta fue del **59,33%**.
- WhatsApp fue el canal con mejor tasa de respuesta, con **70,91%**.
- Email obtuvo **54,24%** e Instagram **50%**.
- Los clientes que respondieron tenían más pedidos previos en promedio.
- Los clientes que respondieron tenían más compras de cafés de origen.
- El uso de cupones previos fue mayor entre quienes respondieron: **84,27%** frente a **67,21%**.
- WhatsApp tuvo resultados especialmente altos en Tucumán, Santa Fe y Córdoba.
- Instagram tuvo un resultado destacado en Entre Ríos, aunque con una cantidad menor de casos.

## Resultado del modelo

El modelo se evaluó sobre 30 registros de prueba y obtuvo:

- Exactitud: **66,67%**.
- Precision para la clase positiva: **67%**.
- Recall para la clase positiva: **89%**.
- F1-score para la clase positiva: **76%**.

La matriz de confusión fue:

```text
[[ 4  8]
 [ 2 16]]
```

El modelo identificó correctamente a **16 de los 18 clientes que respondieron**, aunque también generó 8 falsos positivos. Esto significa que marcó como potenciales compradores a algunos clientes que finalmente no realizaron una compra.

## Variables más influyentes

Las variables con mayor influencia positiva en el modelo fueron:

1. `PedidosDeOrigen`.
2. `UsoCuponPrevio`.
3. `Canal_WhatsApp`.
4. `PedidosPrevios`.
5. `DiasDesdeUltimaCompra`.

En términos comerciales, el perfil con mayor probabilidad de responder es un cliente frecuente, con antecedentes de compra de cafés de origen, acostumbrado a utilizar cupones y contactado por WhatsApp.

## Conclusiones

El análisis permitió identificar patrones asociados con una mayor respuesta a la campaña. Los clientes frecuentes, acostumbrados a utilizar descuentos y con antecedentes de compra de cafés de origen mostraron mayor predisposición a adquirir el producto promocionado.

WhatsApp fue el canal con mejor desempeño general y resultó especialmente efectivo en algunas provincias. A partir de estos resultados, la empresa podría priorizar este canal para clientes con un perfil de alto interés y utilizar los demás canales como alternativas de contacto.

El modelo de regresión logística logró detectar la mayoría de los clientes que respondieron, aunque también generó falsos positivos. Por eso puede utilizarse como una herramienta de apoyo para priorizar clientes y optimizar campañas, pero no como una decisión automática definitiva.

## Limitaciones

- El dataset contiene 150 registros y el conjunto de prueba contiene 30 casos.
- Los datos son ficticios y fueron construidos con fines de aprendizaje.
- Las relaciones encontradas no prueban causalidad.
- El análisis se basa en una única campaña.
- No se compararon varios algoritmos ni se realizó validación cruzada.
- No se incorporaron costos reales de descuentos, publicidad o contacto.
- Antes de aplicar el modelo en un entorno real sería necesario contar con más campañas, resultados históricos y controles de calidad.

## Archivos

- `brava_cafe_campania.xlsx`: modelo de datos y dataset utilizado.
- `analisis_campania.py`: código Python del análisis y del modelo.
- `requirements.txt`: librerías necesarias para ejecutar el proyecto.
