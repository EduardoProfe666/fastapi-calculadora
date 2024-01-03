from pydantic import BaseModel, Field


class DatosDescuentoInicio(BaseModel):
    precio_original: float = Field(ge=0)
    descuento_porciento: float = Field(ge=0)
