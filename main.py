import hashlib
import hmac
import base64

from fastapi import FastAPI, Form, Cookie
from fastapi.responses import Response
from typing import Optional
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/templates", StaticFiles(directory="templates"), name="templates")


database = {
    "focus": {
        "name": "kostya",
        "password": "d8fa8488d7ac553529c7f21ae9a9081713f0e89f28316fb9b1706996ab0f8b7f"
    }
}

# for example. use ENV in future
SECRET_KEY = "98288a54b00ffaaefe4d66bd71becb050d4db3aadb2590e7b8fbe3f74656604"
PASSWORD_SALT = "a6e975ceb69c40e1895c7bda2e34d419eae2ed286eb0eca1a6c1509d932be157"


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
        valid_sign = sign_data(username)
    except Exception:
        return None

    if hmac.compare_digest(sign, valid_sign):
        return username
    return None


def verify_password(password: str, password_hash: str) -> bool:
    return hashlib.sha256((password + PASSWORD_SALT).encode()).hexdigest().lower() == password_hash.lower()


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
    if not user or not verify_password(password, user["password"]):
        return Response("Я вас не знаю", media_type="text/html")

    response = Response(f"Hello, {username}. (привет)", media_type="text/html")

    username_signed = base64.b64encode(username.encode()).decode() + "." + sign_data(username)
    response.set_cookie(key="username", value=username_signed)
    return response


# @app.get("/templates/style.css")
# def index_page():
#     with open("templates/style.css", "r") as fd:
#         css_login_page = fd.read().encode()
#
#     return Response(css_login_page, media_type="text/css")

