from fastapi import Cookie, Response, APIRouter

from typing import Optional

from app.db import data
from app.internal import crypto
from app.services.reader import read_file

router = APIRouter()


@router.get("/")
def index_page(username: Optional[str] = Cookie(default=None)):
    login_page = read_file("static/html/login.html")

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
