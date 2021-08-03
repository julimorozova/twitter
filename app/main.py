from fastapi import FastAPI
from app.routers import api

from fastapi.staticfiles import StaticFiles


# if __name__ == "__main__":
app = FastAPI()
app.include_router(api.router)
app.mount("/templates", StaticFiles(directory="templates"), name="templates")