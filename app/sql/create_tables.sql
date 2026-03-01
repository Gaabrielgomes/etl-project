CREATE TABLE IF NOT EXISTS client_month_total (
    client_id SERIAL UNIQUE PRIMARY,
    month DATE,
    total FLOAT(15, 2)
);

CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL UNIQUE PRIMARY,
    client_id INTEGER,
    value FLOAT(15, 2),
    date TIMESTAMP
);