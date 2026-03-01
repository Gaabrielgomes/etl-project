import pandas as pd
from sqlalchemy import text
from app.db.connection import engine


def extract_transactions(query_path):
    with open(query_path, 'r', encoding='utf-8') as raw_query:
        text_query = text(raw_query.read())
    
    with engine.connect() as connection:
        df = pd.read_sql(text_query, connection)

    return df