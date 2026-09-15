-- 1. Volumen de alertas por mes
SELECT
    DATE_TRUNC('month', alert_date) AS month,
    COUNT(*) AS total_alerts
FROM alerts
GROUP BY 1
ORDER BY 1;

-- 2. Casos abiertos que requieren seguimiento operativo
SELECT
    alert_id,
    alert_date,
    rule_name,
    risk_score,
    severity,
    status
FROM alerts
WHERE status IN ('in_review', 'escalated')
ORDER BY risk_score DESC, alert_date;

-- 3. Cumplimiento de SLA por severidad
SELECT
    severity,
    COUNT(*) AS resolved_alerts,
    SUM(CASE WHEN resolution_hours <= sla_hours THEN 1 ELSE 0 END) AS within_sla,
    ROUND(
        100.0 * SUM(CASE WHEN resolution_hours <= sla_hours THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0),
        2
    ) AS sla_compliance_pct
FROM alerts
WHERE resolution_hours IS NOT NULL
GROUP BY severity
ORDER BY sla_compliance_pct;

-- 4. Reglas con mayor proporción de falsos positivos
SELECT
    rule_name,
    COUNT(*) AS total_alerts,
    SUM(CASE WHEN resolution_type = 'false_positive' THEN 1 ELSE 0 END) AS false_positives,
    ROUND(
        100.0 * SUM(CASE WHEN resolution_type = 'false_positive' THEN 1 ELSE 0 END)
        / NULLIF(COUNT(*), 0),
        2
    ) AS false_positive_rate_pct
FROM alerts
WHERE status = 'closed'
GROUP BY rule_name
ORDER BY false_positive_rate_pct DESC;

-- 5. Alertas de alto riesgo por segmento y canal
SELECT
    customer_segment,
    channel,
    COUNT(*) AS high_risk_alerts,
    SUM(amount_usd) AS amount_under_review
FROM alerts
WHERE risk_score >= 75
GROUP BY customer_segment, channel
ORDER BY high_risk_alerts DESC, amount_under_review DESC;
