# Diccionario de datos

| Campo | Descripción |
|---|---|
| `alert_id` | Identificador único de la alerta. |
| `alert_date` | Fecha de creación de la alerta. |
| `customer_segment` | Segmento simulado del cliente. |
| `channel` | Canal donde se originó la transacción. |
| `rule_name` | Regla que generó la alerta. |
| `amount_usd` | Importe de la transacción en dólares simulados. |
| `risk_score` | Puntaje de riesgo entre 0 y 100. |
| `status` | Estado operativo: cerrada, en revisión o escalada. |
| `severity` | Severidad asignada a la alerta. |
| `resolution_type` | Resultado del análisis: falso positivo o riesgo confirmado. |
| `resolution_hours` | Horas utilizadas para resolver el caso. |

## Reglas de negocio

- SLA crítico: 8 horas.
- SLA alto: 12 horas.
- SLA medio: 24 horas.
- SLA bajo: 48 horas.
- Una alerta está abierta si su estado es `in_review` o `escalated`.
- Se considera falso positivo cuando `resolution_type = false_positive`.
