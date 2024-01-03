from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from router.otros import router as otros
from router.calculo_basico import router as calculo_basico
from router.trigonometria import router as trigonometria
from router.calculadora import router as calculadora
from router.conversion import router as conversion
from router.paginas import router as paginas

# Run with uvicorn main:app --reload

description = """
## ⚓ Listado de Funcionalidades
### 🤓 Cálculo Básico
- Sumar
- Restar
- Multiplicar
- Dividir
- Módulo
- Raíz n-ésima 
- Potenciación
- Logaritmo

### 🤖 Conversión
- Ángulo
- Área
- Datos
- Longitud
- Masa
- Velocidad
- Sistema Numérico (BIN, DEC, HEX, OCT)
- Temperatura
- Tiempo
- Volumen
- Divisas (+160 divisas en tiempo real la tasa de cambio)

### 💥 Trigonometría
- Seno
- Coseno
- Tangente
- Cotangente
- Secante
- Cosecante

### 🎓 Calculadora
- Evaluación y Cálculo de expresiones
- Descuento
- IMC

### 🎈 Otros
- Constantes
"""

app = FastAPI(title="Api Calculadora Simple",
              description=description,
              summary="Api de Calculadora simple desarrollada con FastApi 🚀",
              version="1.0.1",
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

app.include_router(calculo_basico)
app.include_router(calculadora)
app.include_router(trigonometria)
app.include_router(conversion)
app.include_router(otros)
app.include_router(paginas)


@app.exception_handler(404)
async def http_exception_404(request, exc):
    return templates.TemplateResponse("error.html", {
        "request": request,
        "first_digit": "4",
        "second_digit": "0",
        "third_digit": "4",
        "codigo": "404",
        "mensaje": "Página/Servicio no encontrado"
    }, status_code=404)


@app.exception_handler(422)
async def http_exceptio_422(request, exc):
    return templates.TemplateResponse("error.html", {
        "request": request,
        "first_digit": "4",
        "second_digit": "2",
        "third_digit": "2",
        "codigo": "422",
        "mensaje": "Error de validación. Revise la validez de los datos proporcionados."
    }, status_code=422)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    codigo = str(exc.status_code)
    return templates.TemplateResponse("error.html", {
        "request": request,
        "first_digit": codigo[0],
        "second_digit": codigo[1],
        "third_digit": codigo[2],
        "codigo": codigo,
        "mensaje": exc.detail
    }, status_code=exc.status_code)
