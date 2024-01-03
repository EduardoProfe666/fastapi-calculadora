import math

from fastapi import APIRouter

from requests import get
from errors.errors import error_handler
from models.resultadofloat import ResultadoFloat
from models.resultadostr import ResultadoStr
from models.unidades_de_medida import Area, Datos, Longitud, Masa, Sistema_Numerico, Velocidad, Temperatura, Tiempo, \
    Volumen, Angulo, Divisa

router = APIRouter(prefix="/conversion", tags=["Conversión"], responses={400: {"description": "Bad Request"}})


@router.get("/area/", summary="Permite la conversión en unidades de área", response_model=ResultadoFloat)
async def area(num: float, unidad1: Area, unidad2: Area):
    try:
        if num < 0:
            raise ArithmeticError()
        conversions = {
            'm2': 1, 'km2': 1e6, 'ha': 1e4, 'are': 100, 'dm2': 0.01, 'cm2': 1e-4, 'mm2': 1e-6,
            'micrometro2': 1e-12, 'acre': 4046.86, 'milla2': 2.59e6, 'yd2': 0.836127, 'ft2': 0.092903,
            'in2': 0.00064516, 'rd2': 25.2929, 'qing': 6.66667e5, 'chi2': 0.092903, 'cun2': 0.000092903, 'gongli2': 1e6
        }

        return {"resultado": num * conversions[unidad1] / conversions[unidad2]}
    except Exception:
        raise error_handler(cod_error=400, message="Error de conversión. Compruebe que <num> sea >= 0")


@router.get("/datos/", summary="Permite la conversión en unidades de datos. Nota: 1 KB = 1024 B",
            response_model=ResultadoFloat)
async def datos(num: float, unidad1: Datos, unidad2: Datos):
    try:
        if num < 0:
            raise ArithmeticError()
        unidades = ["B", "KB", "MB", "GB", "TB", "PB"]
        factor_conversion = unidades.index(unidad1) - unidades.index(unidad2)

        converted_number = num * (1024 ** factor_conversion)

        return {"resultado": converted_number}
    except Exception:
        raise error_handler(cod_error=400, message="Error de conversión. Compruebe que <num> sea >= 0")


@router.get("/longitud/", summary="Permite la conversión en unidades de longitud.", response_model=ResultadoFloat)
async def longitud(num: float, unidad1: Longitud, unidad2: Longitud):
    try:
        if num < 0:
            raise ArithmeticError()
        unidades = {
            "km": 1e3, "m": 1, "dm": 1e-1, "cm": 1e-2, "mm": 1e-3, "micrometro": 1e-6,
            "nanometro": 1e-9, "picometro": 1e-12, "nmi": 1852, "mi": 1609.34, "fur": 201.168,
            "ftm": 1.8288, "yd": 0.9144, "ft": 0.3048, "in": 0.0254, "gongli": 500, "li": 500,
            "chi": 0.333, "cun": 0.0333, "fen": 0.00333, "lii": 0.000333, "parsec": 3.086e+16,
            "distancia-lunar": 3.844e+8, "unidad-astronomica": 1.496e+11, "anno-luz": 9.461e+15
        }

        return {"resultado": num * (unidades[unidad1] / unidades[unidad2])}
    except Exception:
        raise error_handler(cod_error=400, message="Error de conversión. Compruebe que <num> sea >= 0")


@router.get("/masa/", summary="Permite la conversión en unidades de masa.", response_model=ResultadoFloat)
async def masa(num: float, unidad1: Masa, unidad2: Masa):
    try:
        if num < 0:
            raise ArithmeticError()
        unidades = {
            "t": 1e6, "kg": 1e3, "g": 1, "mg": 1e-3, "microgramo": 1e-6, "quintal": 1e5,
            "lb": 453.59237, "oz": 28.349523125, "carat": 0.2, "grano": 0.06479891
        }

        return {"resultado": num * (unidades[unidad1] / unidades[unidad2])}
    except Exception:
        raise error_handler(cod_error=400, message="Error de conversión. Compruebe que <num> sea >= 0")


@router.get("/velocidad/", summary="Permite la conversión en unidades de velocidad.", response_model=ResultadoFloat)
async def velocidad(num: float, unidad1: Velocidad, unidad2: Velocidad):
    try:
        if num < 0:
            raise ArithmeticError()
        unidades = {
            "c": 299792458, "Ma": 340.29, "m-s": 1, "km-h": 1 / 3.6, "km-s": 1000,
            "kn": 0.514444, "mph": 0.44704, "fps": 0.3048, "ips": 0.0254
        }

        return {"resultado": num * (unidades[unidad1] / unidades[unidad2])}
    except Exception:
        raise error_handler(cod_error=400, message="Error de conversión. Compruebe que <num> sea >= 0")


@router.get("/temperatura/", summary="Permite la conversión en unidades de temperatura.", response_model=ResultadoFloat)
async def temperatura(num: float, unidad1: Temperatura, unidad2: Temperatura):
    try:
        if num < 0:
            raise ArithmeticError()
        if unidad1 == "fahrenheit":
            num = (num - 32) * 5 / 9
        elif unidad1 == "kelvin":
            num = num - 273.15
        elif unidad1 == "rankine":
            num = (num - 491.67) * 5 / 9
        elif unidad1 == "reaumur":
            num = num * 5 / 4

        if unidad2 == "fahrenheit":
            num = num * 9 / 5 + 32
        elif unidad2 == "kelvin":
            num = num + 273.15
        elif unidad2 == "rankine":
            num = (num + 273.15) * 9 / 5
        elif unidad2 == "reaumur":
            num = num * 4 / 5

        return {"resultado": num}
    except Exception:
        raise error_handler(cod_error=400, message="Error de conversión. Compruebe que <num> sea >= 0")


@router.get("/tiempo/", summary="Permite la conversión en unidades de tiempo.", response_model=ResultadoFloat)
async def tiempo(num: float, unidad1: Tiempo, unidad2: Tiempo):
    try:
        if num < 0:
            raise ArithmeticError()
        unidades = {
            "anno": 60 * 60 * 24 * 365,
            "semana": 60 * 60 * 24 * 7,
            "dia": 60 * 60 * 24,
            "hora": 60 * 60,
            "minuto": 60,
            "segundo": 1,
            "milisegundo": 1e-3,
            "microsegundo": 1e-6,
            "picosegundo": 1e-12,
        }

        return {"resultado": num * (unidades[unidad1] / unidades[unidad2])}
    except Exception:
        raise error_handler(cod_error=400, message="Error de conversión. Compruebe que <num> sea >= 0")


@router.get("/volumen/", summary="Permite la conversión en unidades de volumen.", response_model=ResultadoFloat)
async def volumen(num: float, unidad1: Volumen, unidad2: Volumen):
    try:
        if num < 0:
            raise ArithmeticError()
        unidades = {
            "m3": 1,
            "dm3": 1e-3,
            "cm3": 1e-6,
            "mm3": 1e-9,
            "hl": 0.1,
            "l": 1e-3,
            "dl": 1e-4,
            "cl": 1e-5,
            "ml": 1e-6,
            "ft3": 0.0283168,
            "in3": 0.000016387064,
            "yd3": 0.764554858,
            "af3": 1233.48183754752
        }

        return {"resultado": num * (unidades[unidad1] / unidades[unidad2])}
    except Exception:
        raise error_handler(cod_error=400, message="Error de conversión. Compruebe que <num> sea >= 0")


@router.get("/angulo/",
            summary="Permite la conversión de unidades de ángulo (radianes-grados). Nota: Si la unidad de destino es radianes, se asume que la unidad inicial es grados, y viceversa.",
            response_model=ResultadoFloat)
async def angulo(num: float, unidad_destino: Angulo):
    try:
        resultado = 0
        if unidad_destino == "radianes":
            resultado = math.radians(num)
        else:
            resultado = math.degrees(num)

        return {"resultado": resultado}
    except Exception:
        raise error_handler(cod_error=400, message="Error de conversión.")


@router.get("/sistema-numerico/", summary="Permite la conversión de sistema numérico. No admite números fraccionarios.",
            response_model=ResultadoStr)
async def sistema_numerico(num: str, unidad1: Sistema_Numerico, unidad2: Sistema_Numerico):
    try:
        numero = 0
        if unidad1 == "BIN":
            numero = int(num, 2)
        elif unidad1 == "OCT":
            numero = int(num, 8)
        elif unidad1 == "DEC":
            numero = int(num, 10)
        elif unidad1 == "HEX":
            numero = int(num, 16)

        result = 0
        if unidad2 == "BIN":
            result = bin(numero).replace("0b", "")
        elif unidad2 == "OCT":
            result = oct(numero).replace("0o", "")
        elif unidad2 == "HEX":
            result = hex(numero).replace("0x", "")
        elif unidad2 == "DEC":
            result = str(numero)

        return {"resultado": str(result)}
    except Exception:
        raise error_handler(cod_error=400, message="Error de conversión. Compruebe que el número sea válido")


@router.get("/divisas/", summary="Permite la conversión de las divisas según la tasa de cambio en tiempo real.",
            response_model=ResultadoFloat)
async def divisas(num: float, unidad1: Divisa, unidad2: Divisa):
    try:
        if num < 0:
            raise ArithmeticError()

        p = {"api_key": "f6e7ecb95974a2982eaf7f80cdb3eed7cfbc64d6",
             "from": unidad1,
             "to": unidad2,
             "amount": num,
             "format": "json"}
        r = get('https://api.getgeoapi.com/v2/currency/convert', params=p, timeout=5)
        return {"resultado": float(r.json().get('rates').get(unidad2).get('rate_for_amount'))}
    except Exception:
        raise error_handler(cod_error=400, message="Error de conversión.")
