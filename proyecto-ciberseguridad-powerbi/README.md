# SOC Incident & SLA Dashboard

Proyecto de portfolio para mostrar un flujo completo de datos aplicado a ciberseguridad:

1. Partir de una exportación CSV desordenada de incidentes de un SOC.
2. Limpiar y estandarizar los datos con Python/pandas.
3. Crear métricas operativas y de SLA.
4. Construir un informe interactivo en Power BI.

> Todos los datos son ficticios y fueron creados únicamente con fines demostrativos. No representan información de INSSIDE ni de ningún cliente real.

## Estructura

- `data/incidentes_raw.csv`: fuente simulada con duplicados, mayúsculas/minúsculas inconsistentes, espacios, fechas en formatos distintos y valores faltantes.
- `etl_limpieza.py`: proceso reproducible de limpieza y generación de métricas.
- `output/incidentes_limpios.csv`: detalle listo para importar en Power BI.
- `output/kpis_por_mes.csv`: resumen mensual para validar el dashboard.
- `output/catalogo_campos.csv`: diccionario de datos.

## Cómo ejecutarlo

```bash
pip install pandas
python etl_limpieza.py
```

## Métricas sugeridas en Power BI

- Incidentes totales
- Incidentes críticos
- % dentro del SLA de respuesta
- Tiempo medio de respuesta
- Tiempo medio de resolución
- Incidentes abiertos
- Incidentes por cliente, categoría y severidad
- Evolución mensual de incidentes

## Diseño sugerido del informe

### Página 1 — Resumen ejecutivo

Tarjetas de KPI, línea de incidentes por mes, barras por severidad y dona por estado. Agregar segmentadores de fecha, cliente y severidad.

### Página 2 — Operación del SOC

Tabla de incidentes con drill-through, barras por categoría y analista, y dispersión de tiempo de respuesta vs. tiempo de resolución.

### Página 3 — SLA y calidad de servicio

Cumplimiento por cliente, tendencia mensual, matriz de severidad vs. cumplimiento y tabla de incidentes fuera de SLA.

## Texto breve para LinkedIn

> Desarrollé un dashboard de operaciones de ciberseguridad en Power BI a partir de datos simulados de un SOC. Construí un flujo ETL en Python para detectar duplicados, normalizar categorías y fechas, tratar valores faltantes y calcular métricas de SLA. El informe permite analizar volumen, severidad, tiempos de respuesta y resolución por cliente y período.

## Preguntas que el proyecto responde

- ¿Qué clientes concentran más incidentes?
- ¿Qué categorías y severidades requieren más atención?
- ¿El SOC responde dentro del SLA acordado?
- ¿Qué analistas o períodos muestran mayor carga operativa?
- ¿Qué incidentes siguen abiertos o excedieron los tiempos objetivo?
