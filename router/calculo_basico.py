import math
from fastapi import APIRouter
from errors.errors import error_handler
from models.resultadofloat import ResultadoFloat

router = APIRouter(prefix="/calculo-basico", tags=["Cálculo Básico"], responses={400: {"description": "Bad Request"}})


@router.get("/sumar/", summary="Permite sumar 2 números (num1 + num2)", response_model=ResultadoFloat)
async def sumar(num1: float, num2: float):
    try:
        return ResultadoFloat(resultado=num1 + num2)
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/restar/", summary="Permite restar 2 números (num1 - num2)", response_model=ResultadoFloat)
async def restar(num1: float, num2: float):
    try:
        return ResultadoFloat(resultado=num1 - num2)
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/multiplicar/", summary="Permite multiplicar 2 números (num1 * num2)", response_model=ResultadoFloat)
async def multiplicar(num1: float, num2: float):
    try:
        return ResultadoFloat(resultado=num1 * num2)
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/dividir/", summary="Permite dividir 2 números (num1 / num2)", response_model=ResultadoFloat)
async def dividir(num1: float, num2: float):
    try:
        return ResultadoFloat(resultado=num1 / num2)
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/modulo/", summary="Permite calcular el módulo dados 2 números (num1 % num2)",
            response_model=ResultadoFloat)
async def modulo(num1: float, num2: float):
    try:
        return ResultadoFloat(resultado=num1 % num2)
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/raiz/", summary="Permite calcular la raíz n-ésima de un número (radicando ^ 1/radical)",
            response_model=ResultadoFloat)
async def raiz(radicando: float, radical: float):
    try:
        return ResultadoFloat(resultado=math.pow(radicando, 1 / radical))
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/potenciacion/", summary="Permite calcular la potenciación n-ésima de un número (base ^ exponente)",
            response_model=ResultadoFloat)
async def potenciacion(base: float, exponente: float):
    try:
        return ResultadoFloat(resultado=math.pow(base, exponente))
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/logaritmo/", summary="Permite calcular el logaritmo n-ésimo de un número (logbase argumento)",
            response_model=ResultadoFloat)
async def logaritmo(base: float, argumento: float):
    try:
        return ResultadoFloat(resultad=math.log(argumento, base))
    except Exception:
        raise error_handler(cod_error=400)


@router.get("/logaritmo-natural/", summary="Permite calcular el logaritmo natural de un número (lg argumento)",
            response_model=ResultadoFloat)
async def logaritmo_natural(argumento: float):
    try:
        return ResultadoFloat(resultado=math.log(argumento))
    except Exception:
        raise error_handler(cod_error=400)
