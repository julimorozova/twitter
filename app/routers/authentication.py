import json

from fastapi import Form, Cookie, Response, APIRouter, Body

import base64

from app.db.data import data
from app.internal import crypto
from app.services.reader import read_file


router = APIRouter()


@router.post("/login")
def process_login_page(request_data: dict = Body(...)):
    try:
        username = request_data['username']
        password = request_data['password']
    except KeyError:
        return Response(
            json.dumps({
                "success": False,
                "message": "Error when parsing data"
            }),
            media_type="application/json"
        )

    status = data.check_auth(username=username, password=password)

    print("Current status = ", status)
    # if not user or not crypto.verify_password(password, user["password"]):
    if not status:
        return Response(
            json.dumps({
                "success": False,
                "message": "I don't know you"
            }),
            media_type="application/json"
        )

    # page_user = read_file("static/html/userpage.html")
    return Response(
            json.dumps({
                "success": True,
                "message": "I have page",
                "page": "/static/html/userpage.html"
            }),
            media_type="application/json"
        )


    # username_signed = base64.b64encode(username.encode()).decode() + "." + crypto.sign_data(username)
    # response.set_cookie(key="username", value=username_signed)

