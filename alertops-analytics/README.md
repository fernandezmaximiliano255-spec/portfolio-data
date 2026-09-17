# AlertOps Analytics

Proyecto de análisis operativo sobre alertas de clientes y transacciones. Los datos son simulados y están diseñados para representar un flujo de backoffice: revisión de alertas, detección de anomalías, clasificación de casos, seguimiento de SLA y generación de métricas para equipos operativos.

## Objetivo

Analizar el volumen y la calidad de las alertas para identificar:

- casos pendientes o fuera de SLA;
- posibles anomalías transaccionales;
- falsos positivos;
- reglas que generan demasiado ruido;
- métricas útiles para priorizar el trabajo del equipo.

## Flujo del proyecto

1. `data/alerts_raw.csv` contiene los datos simulados iniciales.
2. `python/clean_and_analyze.py` valida tipos, normaliza campos y genera métricas.
3. `sql/analysis_queries.sql` contiene consultas para extraer información operativa.
4. `data/alerts_clean.csv` será la fuente preparada para Power BI.

## Tecnologías

- Python: pandas y análisis exploratorio.
- SQL: filtros, agregaciones, SLA y priorización.
- Power BI: dashboard de seguimiento operativo.

## Métricas propuestas

- Alertas totales y evolución mensual.
- Casos por estado, severidad y regla.
- Tiempo promedio de resolución.
- Porcentaje de falsos positivos.
- Cumplimiento de SLA.
- Alertas pendientes por prioridad.
