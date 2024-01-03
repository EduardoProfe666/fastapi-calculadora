from pydantic import BaseModel


class DatosDescuentoFinal(BaseModel):
    precio_final: float
    ahorro: float