from typing import List

from pydantic import BaseModel


class ModaResultado(BaseModel):
    resultado: List[float]