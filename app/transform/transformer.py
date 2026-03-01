import pandas as pd


def get_high_value_transactions(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
    return df[df["value"] > threshold].copy()


def add_month_column(df: pd.DataFrame) -> pd.DataFrame:
    if "date" not in df.columns:
        raise ValueError("DataFrame não possui coluna 'date'")
    
    df_result = df.copy()
    df_result["month"] = df_result["date"].dt.to_period("M").dt.to_timestamp()
    return df_result