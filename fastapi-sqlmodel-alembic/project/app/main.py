from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session, init_db

import os
import time

from starlette.requests import Request


tags_metadata = [
    {"name": "index", "description": "Welcome Zephyrus and best practices."},
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



