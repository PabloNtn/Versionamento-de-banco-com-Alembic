from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session, init_db
from ...models.models_adress import Adress, AdressCreate

router = APIRouter(
    prefix='/adress',
    tags=["adress"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[Adress])
async def get_adresses(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Adress))
    adresses = result.scalars().all()
    return [Adress(cep=adress.cep, street=adress.street, number=adress.number, id=adress.id) for adress in adresses]


@router.post("/")
async def add_adress(adress: AdressCreate, session: AsyncSession = Depends(get_session)):
    adress = Adress(cep=adress.cep, street=adress.street, number=adress.number)
    session.add(adress)
    await session.commit()
    await session.refresh(adress)
    return adress