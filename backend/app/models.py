from pydantic import BaseModel
from typing import List


class City(BaseModel):
    id: int
    name: str
    region: str
    description: str
    highlights: List[str]
    icon: str