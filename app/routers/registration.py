from fastapi import Cookie, Response, APIRouter

from typing import Optional

router = APIRouter()


@router.get("/html/registration.html")
def index_page(username: Optional[str] = Cookie(default=None)):
    with open("templates/html/registration.html", "r") as fd:
        login_page = fd.read().encode()

    response = Response(login_page, media_type="text/html")
    return response