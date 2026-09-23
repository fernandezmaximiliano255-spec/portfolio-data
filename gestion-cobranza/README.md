# Gestión de cobranza

## Resumen ejecutivo

Este proyecto presenta un informe de Power BI desarrollado sobre un dataset ficticio de una empresa argentina dedicada a la gestión de cobranzas. El objetivo es transformar información operativa en indicadores que permitan comprender la composición de la cartera, detectar niveles de riesgo y evaluar el desempeño de las gestiones realizadas.

El análisis integra información de clientes y gestiones de contacto. A partir de los datos se pueden observar los saldos pendientes, los días de mora, el estado de cada cuenta, los resultados de las campañas, los canales utilizados y el monto recuperado.

El dashboard está orientado a responder preguntas de negocio como:

- ¿Cuántos clientes se encuentran en cartera?
- ¿Cuál es el saldo pendiente total?
- ¿Qué tramos de mora concentran mayor deuda?
- ¿Qué campañas y canales recuperan más dinero?
- ¿Qué proporción de gestiones termina en contacto efectivo o promesa de pago?
- ¿Qué clientes requieren una priorización comercial?

## Herramientas utilizadas

- Microsoft Excel para la organización y preparación del dataset.
- Power BI Desktop para el modelado, las medidas DAX y la construcción del informe.
- Power Query para la limpieza y validación de datos.

## Modelo de datos

El archivo contiene información ficticia organizada en tablas de clientes y gestiones. La tabla `Clientes` contiene la identificación, localidad, provincia, estado de cuenta, días de mora y saldo pendiente. La tabla `Gestiones` registra las acciones de contacto, campañas, canales, resultados, compromisos de pago, montos recuperados y fechas.

## Medidas DAX

El informe incluye ocho medidas principales:

1. `Clientes en cartera`: cantidad de clientes únicos.
2. `Saldo pendiente total`: suma de los saldos pendientes.
3. `Gestiones realizadas`: cantidad total de gestiones.
4. `Contactos efectivos`: cantidad de gestiones con contacto efectivo.
5. `Tasa de contacto`: proporción de contactos efectivos sobre las gestiones realizadas.
6. `Monto recuperado total`: suma del monto recuperado.
7. `Promesas de pago`: cantidad de gestiones con compromiso de pago.
8. `Recupero promedio por gestión`: monto recuperado promedio por gestión.

## Columnas calculadas

Se incorporaron dos columnas calculadas en `Clientes`:

- `Tramo de mora`: clasifica a los clientes en 0 a 30 días, 31 a 90 días, 91 a 180 días y más de 180 días.
- `Nivel de saldo`: clasifica como `Saldo regular` los saldos menores a $150.000 y como `Saldo alto` los saldos iguales o superiores a $150.000.

## Páginas del informe

### 1. Resumen general

Presenta las principales tarjetas de indicadores, el monto recuperado por campaña y la distribución de clientes por segmento. Esta página funciona como una vista ejecutiva del estado general de la operación.

### 2. Análisis de cartera de clientes

Permite analizar la deuda según el tramo de mora y el nivel de saldo. También incluye filtros por estado de cuenta y localidad, además de una tabla con los diez clientes de mayor saldo pendiente.

### 3. Rendimiento de campañas y gestiones

Compara los resultados de las campañas y el rendimiento de los canales de contacto. Incluye filtros por campaña y canal, un gráfico de resultados y una tabla con gestiones, contactos efectivos, tasa de contacto, monto recuperado y promesas de pago.

## Principales conclusiones

El informe permite pasar de un listado operativo de clientes y gestiones a una lectura orientada a la toma de decisiones. La segmentación por mora y saldo ayuda a priorizar la cartera, mientras que la comparación de campañas y canales permite reconocer dónde se concentra el recupero.

También se observa la importancia de analizar los resultados junto con sus denominadores: una campaña puede tener muchas gestiones, pero no necesariamente la mejor tasa de contacto o el mayor recupero promedio. Por eso el dashboard combina volumen, efectividad y monto recuperado.
