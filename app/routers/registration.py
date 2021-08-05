import json
from fastapi import Cookie, Response, APIRouter, Body
from typing import Optional

from app.db.data import data

router = APIRouter()


@router.get("/registration.html")
def registration_page(username: Optional[str] = Cookie(default=None)):
    with open("static/html/registration.html", "r") as fd:
        login_page = fd.read().encode()

    response = Response(login_page, media_type="text/html")
    return response


@router.post("/reg")
def process_registration_page(request_data: dict = Body(...)):
    try:
        username = request_data['username']
        password = request_data['password']
        name = request_data['userFirstName']
        surname = request_data['userLastName']
    except KeyError:
        return Response(
            json.dumps({
                "success": False,
                "message": "Error when parsing data"
            }),
            media_type="application/json"
        )

    if data.contains(username):
        return Response(
            json.dumps({
                "success": False,
                "message": "This username is busy"
            }),
            media_type="application/json"
        )

    data.push(username=username, password=password, name=name)

    if data.contains(username):
        return Response(
            json.dumps({
                "success": True,
                "message": "Successfully add new user",
                "page": "/static/html/userpage.html"
            }),
            media_type="application/json"
        )
    else:
        return Response(
            json.dumps({
                "success": False,
                "message": "Failed add new user"
            }),
            media_type="application/json"
        )