from fastapi import APIRouter

from errors.errors import error_handler
from models.constantes import Constante_Matematica
from models.infoimc import InfoIMC
from models.resultadofloat import ResultadoFloat
from models.unidades_de_medida import Longitud, Datos, IMC_Altura, IMC_Peso, Area, Masa, Sistema_Numerico, Velocidad, \
    Temperatura, Tiempo, Volumen, Divisa, Angulo

router = APIRouter(prefix="/otros", tags=["Otros"], responses={400: {"description": "Bad Request"}})


@router.get("/constantes/{nombre}", summary="Permite obtener el valor de una constante matemática",
            response_model=ResultadoFloat)
async def constantes(nombre: Constante_Matematica):
    if nombre == "e":
        return ResultadoFloat(resultado=2.7182818284590452353602874713526624977572)
    elif nombre == "pi":
        return ResultadoFloat(resultado=3.1415926535897932384626433832795028841971)
    elif nombre == "sqrt-2":
        return {"resultado": 1.4142135623730950488016887242096980785696}
    elif nombre == "sqrt-3":
        return {"resultado": 1.7320508075688772935274463415058723669428}
    elif nombre == "sqrt-5":
        return {"resultado": 2.2360679774997896964091736687312762354406}
    elif nombre == "aureo":
        return {"resultado": 1.6180339887498948482045868343656381177203}
    elif nombre == "alfa-feigenbaum":
        return {"resultado": -2.5029078750958928222839028732182157863812}
    elif nombre == "delta-feigenbaum":
        return {"resultado": 4.6692016091029906718532038204662016172581}
    elif nombre == "euler-mascheroni":
        return {"resultado": 0.5772156649015328606065120900824024310421}
    elif nombre == "artin":
        return {"resultado": 0.3739558136192022880547280543464164151116}
    elif nombre == "primos-gemelos":
        return {"resultado": 0.6601618158468695739278121100145557784326}
    elif nombre == "brun":
        return {"resultado": 1.902160582}
    else:
        raise error_handler(cod_error=400, message="No se encuentra disponible la constante dada")

@router.get("/tipos", summary="Permite obtener todos los tipos usados en la api.")
async def tipos():
    return {
        "constantes-matematicas": Constante_Matematica.__args__,
        "info-imc": InfoIMC.__args__,
        "area": Area.__args__,
        "imc-peso": IMC_Peso.__args__,
        "imc-altura": IMC_Altura.__args__,
        "datos": Datos.__args__,
        "longitud": Longitud.__args__,
        "masa": Masa.__args__,
        "sistema-numerico": Sistema_Numerico.__args__,
        "velocidad": Velocidad.__args__,
        "temperatura": Temperatura.__args__,
        "tiempo": Tiempo.__args__,
        "volumen": Volumen.__args__,
        "angulo": Angulo.__args__,
        "divisa": Divisa.__args__
    }