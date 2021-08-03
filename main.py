import hashlib
import hmac
import base64

from fastapi import FastAPI, Form, Cookie
from fastapi.responses import Response
from typing import Optional

app = FastAPI()


database = {
    "focus": {
        "name": "kostya",
        "password": "123"
    }
}

# for example. use ENV in future
SECRET_KEY = "98288a54b00ffaaefe4d66bd71becb050d4db3aadb2590e7b8fbe3f74656604"


def sign_data(data: str) -> str:
    """ Sign data """
    return hmac.new(
        SECRET_KEY.encode(),
        msg=data.encode(),
        digestmod=hashlib.sha256
    ).hexdigest().upper()


def get_username_from_signed_data(data: str) -> Optional[str]:
    try:
        username_base64, sign = data.split('.')
        username = base64.b64decode(username_base64.encode()).decode()
        # print(f"get_username_from_signed_data: {username}")
        valid_sign = sign_data(username)
    except Exception:
        return None

    if hmac.compare_digest(sign, valid_sign):
        return username
    return None


@app.get("/")
def index_page(username: Optional[str] = Cookie(default=None)):
    with open("templates/login.html", "r") as fd:
        login_page = fd.read().encode()

    # delete invalid cookies
    if not username:
        return Response(login_page, media_type="text/html")

    username_after_check = get_username_from_signed_data(username)
    if username_after_check is None:
        response = Response(f"Hello, xakep! :)")
        response.delete_cookie(key="username")
        return response

    response = Response(f"Hello, {database[username_after_check].get('name')}")
    return response


@app.post("/login")
def process_login_page(username: str = Form(...), password: str = Form(...)):
    user = database.get(username)
    if not user or user["password"] != password:
        return Response("Я вас не знаю", media_type="text/html")

    response = Response(f"Hello, {username}. (привет)", media_type="text/html")

    username_signed = base64.b64encode(username.encode()).decode() + "." + sign_data(username)
    response.set_cookie(key="username", value=username_signed)
    return response
