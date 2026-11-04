import json
from pathlib import Path
from fastapi import HTTPException

from pathlib import Path
import json
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent
CARPETA_MODELOS = BASE_DIR / "modelos"

# Cargar configuración
with open(CARPETA_MODELOS / "configuracion.json", encoding="utf-8") as f:
    configuracion = json.load(f)

with open(CARPETA_MODELOS / "referencia_base.json", encoding="utf-8") as f:
    referencia = json.load(f)

# Cargar únicamente los modelos seleccionados
modelos = {}

for indicador, tipo in configuracion["modelos_seleccionados"].items():
    if tipo == "Random Forest":
        modelos[indicador] = joblib.load(
            CARPETA_MODELOS / f"rf_{indicador}.joblib"
        )
    elif tipo == "Extra Trees":
        modelos[indicador] = joblib.load(
            CARPETA_MODELOS / f"et_{indicador}.joblib"
        )

app = FastAPI(
    title="Malta Predictiva",
    description="API para estimar indicadores de calidad de la malta",
    version="1.0.0"
)

# Datos que recibirá la API
class DatosSecado(BaseModel):
    variedad: str = Field(min_length=1)
    batch_size: float = Field(gt=0)
    tiempo_calentamiento: float = Field(ge=0)
    tiempo_curado: float = Field(ge=0)
    temp_inicio: float
    temp_curado: float
    temp_pre_quiebre: float

@app.get("/")
def inicio():
    return {
        "proyecto": "Malta Predictiva",
        "estado": "API funcionando"
    }

@app.post("/predecir")
def predecir(datos: DatosSecado):


    # Validar rangos históricos con tolerancia del 10 %
    with open(
        Path(__file__).parent / "modelos" / "limites_operativos.json",
        encoding="utf-8"
    ) as archivo:
        limites = json.load(archivo)

    for variable, rango in limites.items():
        valor = getattr(datos, variable)
        minimo = rango["limite_inferior"]
        maximo = rango["limite_superior"]

        if not minimo <= valor <= maximo:
            raise HTTPException(
                status_code=422,
                detail=(
                    f"{variable} fuera del rango histórico permitido: "
                    f"{minimo:.2f} a {maximo:.2f}"
                )
            )

    entrada = pd.DataFrame([datos.model_dump()])

    predicciones = {}

    for indicador, tipo in configuracion["modelos_seleccionados"].items():

        if tipo == "Modelo base":
            variedad = datos.variedad

            medianas = referencia["medianas_por_variedad"].get(
                variedad,
                referencia["mediana_general"]
            )

            valor = medianas[indicador]

        else:
            valor = modelos[indicador].predict(entrada)[0]

        predicciones[indicador] = round(float(valor), 4)

    return {
        "variedad": datos.variedad,
        "predicciones": predicciones
    }


# Mostrar la interfaz web
from fastapi.responses import FileResponse

@app.get("/app", include_in_schema=False)
def mostrar_interfaz():
    return FileResponse(
        BASE_DIR / "web" / "index.html"
    )
