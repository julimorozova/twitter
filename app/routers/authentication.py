from fastapi import Form, Cookie, Response, APIRouter, Body

import base64

from app.db import data
from app.internal import crypto
from app.services.reader import read_file


router = APIRouter()


@router.post("/login")
def process_login_page(request_data: dict = Body(...)):
    username = request_data['username']
    password = request_data['password']

    user = data.database.get(username)
    if not user or not crypto.verify_password(password, user["password"]):
        return Response("Я вас не знаю", media_type="text/html")

    page_user = read_file("static/html/userpage.html")
    response = Response(page_user, media_type="text/html")

    username_signed = base64.b64encode(username.encode()).decode() + "." + crypto.sign_data(username)
    response.set_cookie(key="username", value=username_signed)
    return response



