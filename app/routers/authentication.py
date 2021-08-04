from fastapi import Form, Cookie, Response, APIRouter

import base64

from app.db import data
from app.internal import crypto

router = APIRouter()


@router.post("/login")
def process_login_page(username: str = Form(...), password: str = Form(...)):
    user = data.database.get(username)
    if not user or not crypto.verify_password(password, user["password"]):
        return Response("Я вас не знаю", media_type="text/html")

    response = Response(f"Hello, {username}. (привет)", media_type="text/html")

    username_signed = base64.b64encode(username.encode()).decode() + "." + crypto.sign_data(username)
    response.set_cookie(key="username", value=username_signed)
    return response



