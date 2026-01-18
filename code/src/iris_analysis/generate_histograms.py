"""CLI script that loads the Iris dataset and plots histograms."""

from __future__ import annotations

import argparse
import os
from pathlib import Path

try:
    from .data import load_iris_data
    from .plotting import plot_histograms
except ImportError:  # pragma: no cover - fallback when run as script
    import sys

    PACKAGE_ROOT = Path(__file__).resolve().parent
    if str(PACKAGE_ROOT) not in sys.path:
        sys.path.insert(0, str(PACKAGE_ROOT))

    from data import load_iris_data  # type: ignore  # pylint: disable=import-error
    from plotting import plot_histograms  # type: ignore  # pylint: disable=import-error


CODE_OCEAN_DATA = Path("/data/iris.csv")
CODE_OCEAN_RESULTS = Path("/results")


def _discover_repo_root() -> Path | None:
    """Best-effort attempt to locate the repository root when running from source."""

    current = Path(__file__).resolve()
    try:
        # ../../.. from this file -> <repo>/code/src/iris_analysis -> <repo>
        return current.parents[3]
    except IndexError:
        return None


def _default_input_path() -> Path:
    """Prefer Code Ocean's /data mount, then fall back to repo/local copies."""

    candidates: list[Path] = []

    env_data_dir = os.environ.get("CODE_OCEAN_DATA_DIR")
    if env_data_dir:
        candidates.append(Path(env_data_dir) / "iris.csv")

    repo_root = _discover_repo_root()
    if repo_root:
        candidates.append(repo_root / "data" / "iris.csv")

    candidates.extend(
        [
            CODE_OCEAN_DATA,
            Path.cwd() / "data" / "iris.csv",
            Path("iris.csv"),
        ]
    )

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return CODE_OCEAN_DATA


def _default_output_dir() -> Path:
    """Outputs should land in /results on Code Ocean."""

    candidates: list[Path] = []

    env_results_dir = os.environ.get("CODE_OCEAN_RESULTS_DIR")
    if env_results_dir:
        candidates.append(Path(env_results_dir))

    repo_root = _discover_repo_root()
    if repo_root:
        candidates.append(repo_root / "results")

    candidates.extend(
        [
            CODE_OCEAN_RESULTS,
            Path.cwd() / "results",
            Path("plots"),
        ]
    )

    for candidate in candidates:
        try:
            candidate.mkdir(parents=True, exist_ok=True)
            return candidate
        except OSError:
            continue

    return Path("plots")


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
        default=_default_input_path(),
        help="Ruta al archivo iris.csv (por defecto /data/iris.csv en Code Ocean)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=_default_output_dir(),
        help="Directorio donde se almacenará la figura (por defecto /results)",
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
