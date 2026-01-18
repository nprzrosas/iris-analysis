"""Plotting helpers for Iris histograms."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Use a non-interactive backend so the script works on headless environments.
matplotlib.use("Agg")

FEATURE_COLUMNS = {
    "sepal.length": "Largo del sépalo (cm)",
    "sepal.width": "Ancho del sépalo (cm)",
    "petal.length": "Largo del pétalo (cm)",
    "petal.width": "Ancho del pétalo (cm)",
}


COLORS = {
    "Setosa": "#1f77b4",
    "Versicolor": "#ff7f0e",
    "Virginica": "#2ca02c",
}


def plot_histograms(
    df: pd.DataFrame,
    output_dir: Path,
    bins: int = 20,
    species_order: Iterable[str] | None = None,
) -> Path:
    """Create histograms by feature and return the saved PNG path."""

    output_dir = output_dir.expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "iris_feature_histograms.png"

    species = list(species_order) if species_order else sorted(df["variety"].unique())
    fig, axes = plt.subplots(2, 2, figsize=(12, 8), constrained_layout=True)

    for ax, (column, label) in zip(axes.flat, FEATURE_COLUMNS.items()):
        for name in species:
            values = df.loc[df["variety"].str.lower() == name.lower(), column]
            if values.empty:
                continue

            color = COLORS.get(name.capitalize(), None)
            ax.hist(
                values,
                bins=bins,
                alpha=0.6,
                label=name.capitalize(),
                color=color,
                edgecolor="black",
                linewidth=0.5,
            )

        ax.set_title(f"Distribución de {label}")
        ax.set_xlabel(label)
        ax.set_ylabel("Frecuencia")

    axes.flat[0].legend(title="Especie", loc="upper right")
    fig.suptitle("Distribución de características del Iris", fontsize=16)
    fig.savefig(output_path, dpi=200)
    plt.close(fig)

    return output_path
