# iris-analysis

Proyecto completo en Python para generar histogramas de las cuatro características
medidas en el dataset Iris (`data/iris.csv`). Los histogramas se guardan en un archivo PNG
para visualizar la distribución de cada característica diferenciada por especie.

## Estructura pensada para Code Ocean

```
.
├── code/        # Código fuente, dependencias y entrypoints
├── data/        # Datos de solo lectura (se copia a /data en el cápsula)
├── scratch/     # Resultados intermedios (persisten entre sesiones)
└── results/     # Productos finales (snapshoteados al cerrar la sesión)
```

- `code/src/iris_analysis/`: paquete principal (carga CSV y genera histogramas).
- `code/pyproject.toml` y `code/requirements.txt`: dependencias y script `iris-histograms`.
- `data/iris.csv`: dataset de entrada que debes adjuntar como *data asset* en Code Ocean.
- `results/`: carpeta de salida por defecto (`iris_feature_histograms.png`).

## Configuración local

```bash
cd code
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Ejecución

Desde el directorio `code/` una vez instalado el paquete:

```bash
python -m iris_analysis.generate_histograms  # usa ../data e imprime la ruta del PNG
```

La CLI detecta automáticamente la ubicación del dataset y escribe la imagen en `../results`.
Puedes controlar los parámetros manualmente:

```bash
iris-histograms --input ../data/iris.csv --output-dir ../results --bins 20
```

## Uso dentro de Code Ocean

1. Copia el contenido de este repositorio en el directorio `code/` de la cápsula.
2. Adjunta `data/iris.csv` como *data asset* para que esté disponible en `/data/iris.csv`.
3. En la cápsula ejecuta:

```bash
pip install -r code/requirements.txt
pip install -e code
python -m iris_analysis.generate_histograms  # lee /data y escribe en /results
```

El comando crea `/results/iris_feature_histograms.png`, que quedará incluido en el snapshot
de resultados de Code Ocean.
