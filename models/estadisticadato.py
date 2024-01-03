from typing import List

from pydantic import BaseModel


class EstadisticaDato(BaseModel):
    lista: List[float]
