from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette_prometheus import metrics, PrometheusMiddleware

from app.db import get_session, init_db

import os
import time

from starlette.requests import Request

from .core.songs import songs
from .core.enderecos import enderecos as adress


tags_metadata = [
    {"name": "songs", "description": "Songs Repository."},
    {"name": "adress","description":"Adress Repository"}
]

_prefix_api = os.getenv('PREFIX_API', "/motor")

api_version = "0.1.1"
app = FastAPI(
    title="songs", 
    version=api_version,
    description="songs", 
    openapi_tags=tags_metadata,
    docs_url=f"{_prefix_api}/", 

    openapi_url=f"{_prefix_api}/openapi.json",

)
app.router.redirect_slashes = False
app.include_router(adress.router, prefix=f"{_prefix_api}")
app.include_router(songs.router, prefix=f"{_prefix_api}")


# @app.on_event("startup")
# async def on_startup():
#     await init_db()
# @app.on_event("startup")
# async def on_startup():
#     await init_db()

# @app.middleware("http")
# async def db_session_middleware(request: Request, call_next):
#     start_time = time.time()

#     response = await call_next(request)
#     process_time = time.time() - start_time
    
#     response.headers["X-Process-Time"] = str(process_time)
#     return response


# app.add_middleware(PrometheusMiddleware)
# app.add_route(f"{_prefix_api}/metrics/", metrics)


