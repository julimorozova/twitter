from fastapi import FastAPI
from app.routers import api

from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.include_router(api.router)
app.mount("/templates", StaticFiles(directory="templates"), name="templates")