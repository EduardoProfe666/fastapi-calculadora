from fastapi import APIRouter

from errors.errors import error_handler
from models.datos import DatosDescuentoFinal
from models.datosdescuentoinicio import DatosDescuentoInicio
from models.expresion import Expresion
from models.imcdatos import IMCDatos
from models.imcrespuesta import IMCRespuesta
from models.resultadofloat import ResultadoFloat
from models.unidades_de_medida import Masa, Longitud

router = APIRouter(prefix="/calculadora", tags=["Calculadora"], responses={400: {"description": "Bad Request"}})


@router.post("/calcular",
             summary="Permite calcular la expresión matemática simple dada (sin funciones trigonométricas)",
             response_model=ResultadoFloat)
async def calcular(expr: Expresion):
    try:
        return ResultadoFloat(resultado=eval(expr.expr))
    except Exception:
        raise error_handler(cod_error=400, message="La expressión no es válida")


@router.post("/descuento/",
             summary="Permite calcular el descuento dado el precio original y el porcentaje de descuento.",
             response_model=DatosDescuentoFinal)
async def descuento(descuento: DatosDescuentoInicio):
    precio = descuento.precio_original * (100 - descuento.descuento_porciento) / 100
    ahorro = descuento.precio_original - precio
    return DatosDescuentoFinal(precio_final=precio, ahorro=ahorro)


def longitud(num: float, unidad1: Longitud, unidad2: Longitud):
    unidades = {
        "km": 1e3, "m": 1, "dm": 1e-1, "cm": 1e-2, "mm": 1e-3, "micrometro": 1e-6,
        "nanometro": 1e-9, "picometro": 1e-12, "nmi": 1852, "mi": 1609.34, "fur": 201.168,
        "ftm": 1.8288, "yd": 0.9144, "ft": 0.3048, "in": 0.0254, "gongli": 500, "li": 500,
        "chi": 0.333, "cun": 0.0333, "fen": 0.00333, "lii": 0.000333, "parsec": 3.086e+16,
        "distancia-lunar": 3.844e+8, "unidad-astronomica": 1.496e+11, "anno-luz": 9.461e+15
    }

    return num * (unidades[unidad1] / unidades[unidad2])


def masa(num: float, unidad1: Masa, unidad2: Masa):
    unidades = {
        "t": 1e6, "kg": 1e3, "g": 1, "mg": 1e-3, "microgramo": 1e-6, "quintal": 1e5,
        "lb": 453.59237, "oz": 28.349523125, "carat": 0.2, "grano": 0.06479891
    }

    return num * (unidades[unidad1] / unidades[unidad2])


@router.post("/imc/", summary="Permite calcular el índice de masa corporal de una persona dados su peso y altura.",
             response_model=IMCRespuesta)
async def imc(imc_datos: IMCDatos):
    peso = masa(num=imc_datos.peso, unidad1=imc_datos.peso_um, unidad2="kg")
    altura = longitud(num=imc_datos.altura, unidad1=imc_datos.altura_um, unidad2="m")
    r = peso / (altura ** 2)
    info = ""
    if r < 16.5:
        info = "Bajo Peso Severo"
    elif r < 18.5:
        info = "Bajo Peso"
    elif r < 25:
        info = "Peso Normal"
    elif r < 30:
        info = "Sobrepeso"
    elif r < 35:
        info = "Obesidad Moderada"
    elif r < 40:
        info = "Obesidad Severa"
    elif r < 50:
        info = "Obesidad Mórbida"
    else:
        info = "Obesidad Mortal"
    return IMCRespuesta(imc=r, info=info)
