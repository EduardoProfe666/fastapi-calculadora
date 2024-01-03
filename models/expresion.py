from pydantic import BaseModel


class Expresion(BaseModel):
    expr: str
