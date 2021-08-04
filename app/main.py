from fastapi import FastAPI
from app.routers import api

from starlette.applications import Starlette
from starlette.routing import Mount
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.include_router(api.router)

app.mount('/static', app=StaticFiles(directory='static'), name="static"),
