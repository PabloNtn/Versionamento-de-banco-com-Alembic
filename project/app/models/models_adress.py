from sqlmodel import SQLModel, Field
from typing import Optional

class AdressBase(SQLModel):
    cep: int
    street: str
    number: Optional[int] = None


class Adress(AdressBase, table=True):
    id: int = Field(default=None, primary_key=True)


class AdressCreate(AdressBase):
    pass

