# Estructura del proyecto

```text
Fase II/
|
|-- api.py
|-- Dockerfile
|-- .dockerignore
|-- .gitignore
|-- requirements.txt
|-- README.md
|-- MANUAL_DESPLIEGUE.md
|-- ESTRUCTURA_PROYECTO.md
|
|-- web/
|   |-- index.html
|
|-- modelos/
|   |-- configuracion.json
|   |-- referencia_base.json
|   |-- limites_operativos.json
|   |-- metricas_finales.csv
|   |-- archivos .joblib
|
|-- Fase II.ipynb
```

## Componentes

api.py:
Servicio FastAPI, carga de modelos, validación de entradas
y generación de predicciones.

Dockerfile:
Instrucciones para construir la imagen del contenedor.

requirements.txt:
Dependencias y versiones de Python.

web/index.html:
Interfaz web para introducir variables operativas y
visualizar resultados.

modelos/:
Configuración, límites de validación, métricas y
modelos entrenados.

Fase II.ipynb:
Desarrollo experimental y evaluación de modelos.

## Repositorio

Para compartir el código públicamente, se recomienda excluir
los archivos originales PTS y MQI y los modelos entrenados con
información industrial, salvo autorización expresa.

Un repositorio sin los modelos no podrá ejecutar las predicciones
hasta que se incorporen los archivos autorizados.
