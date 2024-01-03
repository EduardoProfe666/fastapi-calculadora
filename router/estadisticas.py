from typing import Optional

from fastapi import APIRouter
import statistics as st

from errors.errors import error_handler
from models.estadisticadato import EstadisticaDato
from models.modaresultado import ModaResultado
from models.resultadofloat import ResultadoFloat

router = APIRouter(prefix='/estadisticas', tags=["Estadísticas"], responses={400: {"description": "Bad Request"}})


@router.post("/media/", summary="Permite determinar la media de un conjunto de elementos",
             response_model=ResultadoFloat)
async def media(datos: EstadisticaDato):
    try:
        return {"resultado": st.mean(datos.lista)}
    except Exception:
        raise error_handler(cod_error=400, message="Error estadístico.")


@router.post("/mediana/", summary="Permite determinar la mediana de un conjunto de elementos",
             response_model=ResultadoFloat)
async def mediana(datos: EstadisticaDato):
    try:
        return {"resultado": st.median(datos.lista)}
    except Exception:
        raise error_handler(cod_error=400, message="Error estadístico.")


@router.post("/moda/",
             summary="Permite determinar la moda de un conjunto de elementos. Funciona también como multi-moda.",
             response_model=ModaResultado)
async def moda(datos: EstadisticaDato):
    try:
        return {"resultado": st.multimode(datos.lista)}
    except Exception:
        raise error_handler(cod_error=400, message="Error estadístico.")


@router.post("/desviacion-poblacion/", summary="Permite determinar la desviación estándar de la población dada",
             response_model=ResultadoFloat)
async def pdesv(datos: EstadisticaDato, mu: float = None):
    try:
        return {"resultado": st.pstdev(datos.lista, mu)}
    except Exception:
        raise error_handler(cod_error=400, message="Error estadístico.")


@router.post("/varianza-poblacion/", summary="Permite determinar la varianza de la población dada",
             response_model=ResultadoFloat)
async def pvar(datos: EstadisticaDato, mu: float = None):
    try:
        return {"resultado": st.pvariance(datos.lista, mu)}
    except Exception:
        raise error_handler(cod_error=400, message="Error estadístico.")


@router.post("/desviacion-muestra/", summary="Permite determinar la desviación estándar de la muestra dada",
             response_model=ResultadoFloat)
async def mdesv(datos: EstadisticaDato, xbar: float = None):
    try:
        return {"resultado": st.stdev(datos.lista, xbar)}
    except Exception:
        raise error_handler(cod_error=400, message="Error estadístico.")


@router.post("/varianza-muestra/", summary="Permite determinar la varianza de la muestra dada",
             response_model=ResultadoFloat)
async def mvar(datos: EstadisticaDato, xbar: float = None):
    try:
        return {"resultado": st.variance(datos.lista, xbar)}
    except Exception:
        raise error_handler(cod_error=400, message="Error estadístico.")


@router.post("/correlacion/", summary="Permite determinar el coeficiente de correlación de Pearson",
             response_model=ResultadoFloat)
async def correlacion(x: EstadisticaDato, y: EstadisticaDato):
    try:
        return {"resultado": st.correlation(x.lista, y.lista)}
    except Exception:
        raise error_handler(cod_error=400, message="Error estadístico.")


@router.post("/covarianza/", summary="Permite determinar la covarianza",
             response_model=ResultadoFloat)
async def covarianza(x: EstadisticaDato, y: EstadisticaDato):
    try:
        return {"resultado": st.covariance(x.lista, y.lista)}
    except Exception:
        raise error_handler(cod_error=400, message="Error estadístico.")
