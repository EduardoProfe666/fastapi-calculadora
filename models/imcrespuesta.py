from pydantic import BaseModel

from models.infoimc import InfoIMC


class IMCRespuesta(BaseModel):
    imc: float
    info: InfoIMC
