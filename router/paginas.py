from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(tags=["Páginas Extras"], responses={400: {"description": "Bad Request"}})

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):

    return templates.TemplateResponse("index.html", {
        "request": request
    })


@router.get("/calculadora", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("p-sec-1.html", {
        "request": request,
        "titulo": "Calculadora"
    })


@router.get("/calculo_basico", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("p-sec-1.html", {
        "request": request,
        "titulo": "Cálculo Básico"
    })


@router.get("/conversion", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("p-sec-1.html", {
        "request": request,
        "titulo": "Conversión"
    })


@router.get("/otros", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("p-sec-1.html", {
        "request": request,
        "titulo": "Otros"
    })


@router.get("/trigonometria", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("p-sec-1.html", {
        "request": request,
        "titulo": "Trigonometría"
    })


