import math
from fastapi import APIRouter
from errors.errors import error_handler
from models.resultadofloat import ResultadoFloat

router = APIRouter(prefix="/trigonometria", tags=["Trigonometría"], responses={400: {"description": "Bad Request"}})


@router.get("/seno/{num}",
            summary="Permite calcular el seno de un número (sen(num))",
            response_model=ResultadoFloat)
async def seno(num: float, es_radian: bool = True):
    try:
        return {"resultado": math.sin(num if es_radian else math.radians(num))}
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/coseno/{num}",
            summary="Permite calcular el coseno de un número (cos(num))",
            response_model=ResultadoFloat)
async def coseno(num: float, es_radian: bool = True):
    try:
        return {"resultado": math.cos(num if es_radian else math.radians(num))}
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/tangente/{num}",
            summary="Permite calcular la tangente de un número (tan(num))",
            response_model=ResultadoFloat)
async def tangente(num: float, es_radian: bool = True):
    try:
        return {"resultado": math.tan(num if es_radian else math.radians(num))}
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/cotangente/{num}",
            summary="Permite calcular la cotangente de un número (cot(num))",
            response_model=ResultadoFloat)
async def cotangente(num: float, es_radian: bool = True):
    try:
        return {"resultado": 1 / math.tan(num if es_radian else math.radians(num))}
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/secante/{num}",
            summary="Permite calcular la secante de un número (sec(num))",
            response_model=ResultadoFloat)
async def secante(num: float, es_radian: bool = True):
    try:
        return {"resultado": 1 / math.cos(num if es_radian else math.radians(num))}
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/cosecante/{num}",
            summary="Permite calcular la cosecante de un número (csc(num))",
            response_model=ResultadoFloat)
async def cosecante(num: float, es_radian: bool = True):
    try:
        return {"resultado": 1 / math.sin(num if es_radian else math.radians(num))}
    except Exception:
        raise error_handler(cod_error=400)
