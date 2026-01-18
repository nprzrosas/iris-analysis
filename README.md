# iris-analysis

Proyecto completo en Python para generar histogramas de las cuatro características
medidas en el dataset Iris (`iris.csv`). Los histogramas se guardan en un archivo PNG
para visualizar la distribución de cada característica diferenciada por especie.

## Requisitos

- Python 3.9+
- [pip](https://pip.pypa.io) o [uv](https://github.com/astral-sh/uv)

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Uso

```bash
iris-histograms --input iris.csv --output-dir plots --bins 20
```

Al finalizar, se creará `plots/iris_feature_histograms.png` con un histograma por
característica (largo/ancho de sépalo y pétalo). Ajusta `--bins` para cambiar la
resolución de los histogramas.

## Estructura

- `iris.csv`: dataset original con las medidas.
- `src/iris_analysis/`: paquete con utilidades de carga y graficado.
- `pyproject.toml`: dependencias y punto de entrada `iris-histograms`.
