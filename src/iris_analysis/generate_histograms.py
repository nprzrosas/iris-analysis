"""CLI script that loads the Iris dataset and plots histograms."""

from __future__ import annotations

import argparse
from pathlib import Path

from .data import load_iris_data
from .plotting import plot_histograms


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Genera histogramas de cada característica del dataset de Iris "
            "y guarda la figura en disco."
        )
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("iris.csv"),
        help="Ruta al archivo iris.csv (por defecto ./iris.csv)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("plots"),
        help="Directorio donde se almacenará la figura",
    )
    parser.add_argument(
        "--bins",
        type=int,
        default=20,
        help="Número de contenedores del histograma",
    )
    return parser


def main(argv: list[str] | None = None) -> Path:
    parser = build_parser()
    args = parser.parse_args(argv)

    df = load_iris_data(args.input)
    output_path = plot_histograms(df, args.output_dir, bins=args.bins)
    print(f"Histogramas guardados en: {output_path}")
    return output_path


if __name__ == "__main__":
    main()
