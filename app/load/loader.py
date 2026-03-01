from sqlalchemy import text
from app.db.connection import engine
import pandas as pd


def read_query_file(query_path: str) -> text:
    with open(query_path, 'r', encoding='utf-8') as file:
        return text(file.read())


def create_tables(query_paths: list[str]):
    with engine.begin() as connection:
        for query_path in query_paths:
            sql_query = read_query_file(query_path)
            connection.execute(sql_query)


def refresh_client_month_total(query_path: str, table_name: str):
    if not table_name.isidentifier():
        raise ValueError(f"Nome de tabela inválido: {table_name}")
    
    with engine.begin() as connection:
        connection.execute(text(f"DELETE FROM {table_name};"))
        
        sql_query = read_query_file(query_path)
        connection.execute(sql_query)


def load_high_value_transactions(table_name: str, df: pd.DataFrame):
    if not table_name.isidentifier():
        raise ValueError(f"Nome de tabela inválido: {table_name}")
    
    with engine.begin() as connection:
        connection.execute(text(f"DELETE FROM {table_name};"))
        
        df.to_sql(
            name=table_name,
            con=connection,
            if_exists='append',
            index=False,
            method='multi'
        )