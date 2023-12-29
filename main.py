import math

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# Run with uvicorn main:app --reload

description = """
## 🤖 Generalidades
Provee de ciertos servicios para realizar las operaciones básicas de una calculadora

## 💫 Listado de operaciones
- **Sumar (_+_)**
- **Restar (_-_)**
- **Multiplicar (_\*_)**
- **Dividir (_/_)**
- **Módulo (_%_)**
- **Raíz n-ésima (_√_)**
- **Potenciación (_n^m_)**
- **Logaritmo (_log(n)_)**
- **Seno (_sin(x)_)**
- **Coseno (_cos(x)_)**
- **Tangente (_tan(x)_)**
- **Cotangente (_cot(x))**
- **Secante (_sec(x)_)**
- **Cosecante (_cot(x)_)**
- **Constantes (_e,pi,..._)**
- **Evaluación y Cálculo de expresiones (_eval(str)_)**
"""

app = FastAPI(title="Api Calculadora Simple",
              description=description,
              summary="Api de Calculadora simple desarrollada con FastApi 🚀",
              version="0.9.5",
              contact={
                  "name": "Eduardo González",
                  "url": "https://github.com/EduardoProfe666",
                  "email": "eduardoglez64377@gmail.com",
              },
              license_info={
                  "name": "MIT License",
                  "url": "https://opensource.org/license/mit/"
              })

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })


@app.get("/sumar/", summary="Permite sumar 2 números (num1 + num2)")
async def sumar(num1: float, num2: float):
    try:
        return {"resultado": num1 + num2}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/restar/", summary="Permite restar 2 números (num1 - num2)")
async def restar(num1: float, num2: float):
    try:
        return {"resultado": num1 - num2}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/multiplicar/", summary="Permite multiplicar 2 números (num1 * num2)")
async def multiplicar(num1: float, num2: float):
    try:
        return {"resultado": num1 * num2}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/dividir/", summary="Permite dividir 2 números (num1 / num2)")
async def dividir(num1: float, num2: float):
    try:
        return {"resultado": num1 / num2}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/modulo/", summary="Permite calcular el módulo dados 2 números (num1 % num2)")
async def modulo(num1: float, num2: float):
    try:
        return {"resultado": num1 % num2}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/raiz/", summary="Permite calcular la raíz n-ésima de un número (radicando ^ 1/radical)")
async def raiz(radicando: float, radical: float):
    try:
        return {"resultado": math.pow(radicando, 1 / radical)}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/potenciacion/", summary="Permite calcular la potenciación n-ésima de un número (base ^ exponente)")
async def potenciacion(base: float, exponente: float):
    try:
        return {"resultado": math.pow(base, exponente)}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/logaritmo/", summary="Permite calcular el logaritmo n-ésimo de un número (logbase argumento)")
async def logaritmo(base: float, argumento: float):
    try:
        return {"resultado": math.log(argumento, base)}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/logaritmo-natural/", summary="Permite calcular el logaritmo natural de un número (lg argumento)")
async def logaritmo_natural(argumento: float):
    try:
        return {"resultado": math.log(argumento)}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/seno/{num}", summary="Permite calcular el seno de un número (sen(num))")
async def seno(num: float):
    try:
        return {"resultado": math.sin(num)}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/coseno/{num}", summary="Permite calcular el coseno de un número (cos(num))")
async def coseno(num: float):
    try:
        return {"resultado": math.cos(num)}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/tangente/{num}", summary="Permite calcular la tangente de un número (tan(num))")
async def tangente(num: float):
    try:
        return {"resultado": math.tan(num)}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/cotangente/{num}", summary="Permite calcular la cotangente de un número (cot(num))")
async def cotangente(num: float):
    try:
        return {"resultado": 1 / math.tan(num)}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/secante/{num}", summary="Permite calcular la secante de un número (sec(num))")
async def secante(num: float):
    try:
        return {"resultado": 1 / math.cos(num)}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/cosecante/{num}", summary="Permite calcular la cosecante de un número (csc(num))")
async def cosecante(num: float):
    try:
        return {"resultado": 1 / math.sin(num)}
    except Exception:
        raise HTTPException(status_code=400,
                            detail="Error en los datos proporcionados. Compruebe los datos. Compruebe que no esté "
                                   "ocurriendo una división por 0")


@app.get("/constantes/{nombre}", summary="Permite obtener el valor de una constante dada (euler|e -> e, pi -> pi)")
async def constantes(nombre: str):
    if nombre == "euler" or nombre == "e":
        return {"resultado": math.e}
    elif nombre == "pi":
        return {"resultado": math.pi}
    else:
        raise HTTPException(status_code=400, detail="No existe la constante dada")


class Auxiliar(BaseModel):
    expr: str


@app.post("/calcular",
          summary="Permite calcular la expresión matemática simple dada (sin funciones trigonométricas)")
async def calcular(expr: Auxiliar):
    try:
        return {"resultado": eval(expr.expr)}
    except Exception:
        raise HTTPException(status_code=400, detail="La expressión no es válida")
