from fastapi import APIRouter, Request, Form
from fastapi_mail import ConnectionConfig, MessageSchema, MessageType, FastMail
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

router = APIRouter(tags=["Páginas Extras"], responses={400: {"description": "Bad Request"}})

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "base": str(request.base_url)
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


@router.get("/estadisticas", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("p-sec-1.html", {
        "request": request,
        "titulo": "Estadísticas"
    })


# @router.post("/email", response_class=HTMLResponse)
# async def root(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...)):
#     conf = ConnectionConfig(
#         MAIL_USERNAME="fastapicalculadora@gmail.com",
#         MAIL_PASSWORD="cxnnzmjekaqbsuyd",
#         MAIL_FROM="fastapicalculadora@gmail.com",
#         MAIL_PORT=587,
#         MAIL_SERVER="smtp.gmail.com",
#         MAIL_FROM_NAME="FastApi Calculadora Simple",
#         MAIL_STARTTLS=True,
#         MAIL_SSL_TLS=False,
#         USE_CREDENTIALS=True,
#         VALIDATE_CERTS=True
#     )
#
#
#     html = f"""
#            <h1>FastApi Calculadora Simple</h1>
#            <h3>Nombre: {name}</h3>
#            <h3>Correo: {email}</h3>
#            <h3>Mensaje:</h3>
#            <p>{message}</p>
#        """
#
#     message = MessageSchema(
#         subject="Formulario de FastApi Calculadora Simple",
#         recipients=["fastapicalculadora@gmail.com"],
#         body=html,
#         subtype=MessageType.html
#     )
#
#     fm = FastMail(conf)
#     await fm.send_message(message)
#
#     return templates.TemplateResponse("p-sec-1.html", {
#         "request": request,
#         "titulo": "Email Enviado"
#     })

@router.post("/email", response_class=HTMLResponse)
async def root(request: Request, name: str = Form(...), email: str = Form(...), message: str = Form(...)):
    return templates.TemplateResponse("p-sec-1.html", {
        "request": request,
        "titulo": "Email Enviado"
    })
