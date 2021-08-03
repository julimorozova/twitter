from fastapi import FastAPI, Form
from fastapi.responses import Response


app = FastAPI()


database = {
    "focus": {
        "password": "123"
    }
}


@app.get("/")
def index_page():
    with open("templates/login.html", "r") as fd:
        login_page = fd.read().encode()
    return Response(login_page, media_type="text/html")


@app.post("/login")
def process_login_page(username: str = Form(...), password: str = Form(...)):
    user = database.get(username)
    if not user or user["password"] != password:
        return Response("Я вас не знаю", media_type="text/html")

    return Response(f"Hello, {username}. (привет)", media_type="text/html")