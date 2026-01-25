# src/data/cleaning.py

import pandas as pd
import numpy as np


def base_clean(feature_store: pd.DataFrame) -> pd.DataFrame:
    """
    Common cleaning applied to all tasks.
    Handles types, basic standardisation.
    """
    df = feature_store.copy()

    # Numeric columns
    num_cols = [
        c for c in df.columns
        if c.startswith("cum_") or c in [
            "week",
            "module_presentation_length",
            "date_registration",
            "date_unregistration",
            "studied_credits",
            "num_of_prev_attempts",
            "weight_covered",
            "target_score",
            "target_score_norm",
        ]
    ]

    for c in num_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")

    # Categorical columns
    cat_cols = [
        "gender",
        "region",
        "highest_education",
        "imd_band",
        "age_band",
        "disability",
        "final_result",
    ]

    for c in cat_cols:
        if c in df.columns:
            df[c] = (
                df[c]
                .astype(str)
                .str.strip()
                .str.lower()
                .replace({"nan": np.nan})
            )

    return df


def clean_for_classification(feature_store: pd.DataFrame) -> pd.DataFrame:
    """
    Cleaning pipeline for early warning classification.
    Target: target_pass (0/1)
    """
    df = base_clean(feature_store)

    # Valid targets only
    df = df[df["target_pass"].notna()]

    # Drop students who withdrew before teaching
    df = df[
        ~(
            df["date_unregistration"].notna() &
            (df["date_unregistration"] < 1)
        )
    ]

    # Drop leakage / irrelevant columns
    df = df.drop(columns=[
        "final_result",
        "date_unregistration",
        "target_score",
        "target_score_norm",
        "weight_covered",
    ], errors="ignore")

    return df


def clean_for_regression(feature_store: pd.DataFrame, min_weight_covered: float = 80) -> pd.DataFrame:
    """
    Cleaning pipeline for final score regression.
    Target: target_score
    """
    df = base_clean(feature_store)

    # Valid scores only
    df = df[df["target_score"].notna()]

    # Require sufficient assessment coverage
    df = df[df["weight_covered"] >= min_weight_covered]

    # Drop classification / leakage columns
    df = df.drop(columns=[
        "final_result",
        "target_pass",
        "date_unregistration",
    ], errors="ignore")

    return df


def split_xy(df: pd.DataFrame, target_col: str):
    """
    Utility: split features and target.
    """
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y
