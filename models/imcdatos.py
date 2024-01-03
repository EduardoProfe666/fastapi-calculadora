from pydantic import BaseModel, Field

from models.unidades_de_medida import IMC_Peso, IMC_Altura


class IMCDatos(BaseModel):
    peso: float = Field(gt=0)
    altura: float = Field(gt=0)
    peso_um: IMC_Peso
    altura_um: IMC_Altura
