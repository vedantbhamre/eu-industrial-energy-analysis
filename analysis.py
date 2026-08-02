import pandas as pd


def add_percent_change(df: pd.DataFrame, start_col: str, end_col: str) -> pd.DataFrame:
    
    result = df.copy()
    result["pct_change"] = (
        (result[end_col] - result[start_col]) / result[start_col] * 100
    ).round(1)
    return result


def rank_by_change(df: pd.DataFrame, ascending: bool = True) -> pd.DataFrame:
    """Sort products/sectors by their percent change"""
    return df.sort_values("pct_change", ascending=ascending).reset_index(drop=True)


def total_decline_summary(total_dict: dict) -> dict:
    years = sorted(total_dict.keys())
    start_year, end_year = years[0], years[-1]
    start_val, end_val = total_dict[start_year], total_dict[end_year]
    pct = round((end_val - start_val) / start_val * 100, 1)
    return {
        "start_year": start_year,
        "end_year": end_year,
        "start_pj": start_val,
        "end_pj": end_val,
        "pct_change": pct,
    }
