"""Data loading utilities for the Iris histogram project."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_iris_data(csv_path: Path) -> pd.DataFrame:
    """Return the Iris dataset stored at *csv_path*.

    Raises:
        FileNotFoundError: If the CSV file does not exist.
        ValueError: If required columns are missing.
    """

    csv_path = csv_path.expanduser().resolve()
    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset not found at {csv_path}")

    df = pd.read_csv(csv_path)
    required_columns = {
        "sepal.length",
        "sepal.width",
        "petal.length",
        "petal.width",
        "variety",
    }
    missing = required_columns.difference(df.columns)
    if missing:
        raise ValueError(
            "Dataset is missing required columns: " + ", ".join(sorted(missing))
        )

    return df
