from fastapi import Form, Cookie, Response, APIRouter

import base64
from typing import Optional

from app.db import data
from app.internal import crypto

router = APIRouter()


@router.get("/")
def index_page(username: Optional[str] = Cookie(default=None)):
    with open("templates/login.html", "r") as fd:
        login_page = fd.read().encode()

    # delete invalid cookies
    if not username:
        return Response(login_page, media_type="text/html")

    username_after_check = crypto.get_username_from_signed_data(username)
    if username_after_check is None:
        response = Response(f"Hello, xakep! :)")
        response.delete_cookie(key="username")
        return response

    response = Response(f"Hello, {data.database[username_after_check].get('name')}")
    return response


@router.post("/login")
def process_login_page(username: str = Form(...), password: str = Form(...)):
    user = data.database.get(username)
    if not user or not crypto.verify_password(password, user["password"]):
        return Response("Я вас не знаю", media_type="text/html")

    response = Response(f"Hello, {username}. (привет)", media_type="text/html")

    username_signed = base64.b64encode(username.encode()).decode() + "." + crypto.sign_data(username)
    response.set_cookie(key="username", value=username_signed)
    return response