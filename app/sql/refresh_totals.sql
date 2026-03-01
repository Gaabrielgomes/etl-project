DELETE FROM client_month_total;

INSERT INTO client_month_total (client_id, month, total)
SELECT
    client_id,
    DATE_TRUNC('month', date) AS month,
    SUM(value) AS total
FROM transactions
GROUP BY client_id, DATE_TRUNC('month', date);