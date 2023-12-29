# 💥 Api Calculadora Simple
Api de Calculadora Simple desarrollada con FastApi 🚀

## 💠 Instalación del proyecto
1. Instalar los requerimientos necesarios con `pip install -r requeriments.txt`
2. Usar el comando `uvicorn main:app --reload` para probar el proyecto
3. Acceder a `localhost:8000/docs` para obtener la documentación de todos los endpoints y poder probarlos
4. Puede probar los endpoints con los tests disponibles en el fichero `test_main.http`

## ⚓ Listado de Funcionalidades
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

## 🔥 Listado de Endpoints
- `GET (...)/`: Página de Inicio de la Api
- `GET (...)/sumar/?num1={}&num2={}`: Operación de suma
- `GET (...)/restar/?num1={}&num2={}`: Operación de resta
- `GET (...)/multiplicar/?num1={}&num2={}`: Operación de multiplicación
- `GET (...)/dividir/?num1={}&num2={}`: Operación de división
- `GET (...)/modulo/?num1={}&num2={}`: Operación de módulo
- `GET (...)/raiz/?radicando={}&radical={}`: Operación de raíz n-ésima
- `GET (...)/potenciacion/?base={}&exponente={}`: Operación de potenciación
- `GET (...)/logaritmo/?base={}&argumento={}`: Operación de logaritmo n-ésimo
- `GET (...)/logaritmo-natural/?argumento={}`: Operación de logaritmo natural
- `GET (...)/seno/{}`: Operación de seno
- `GET (...)/coseno/{}`: Operación de coseno
- `GET (...)/tangente/{}`: Operación de tangente
- `GET (...)/cotangente/{}`: Operación de cotangente
- `GET (...)/secante/{}`: Operación de secante
- `GET (...)/cosecante/{}`: Operación de cosecante
- `GET (...)/constantes/{}`: Obtener constante
- `POST (...)/calcular`: Calcular la expresión dada

## 🛫 Despliegue como Web-Service en `render.com`
Acceda al [siguiente enlace]() para probar la api en vivo
