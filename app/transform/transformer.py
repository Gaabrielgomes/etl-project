import pandas as pd


def calculate_high_value_transactions(df: pd.DataFrame, treshold: float):
    df["is_high_value"] = df["value"] > treshold
    return df[df["is_high_value"] == True].copy()


def add_month_column(df: pd.DataFrame):
    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
    return df