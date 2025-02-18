import fastapi
import fastapi_chameleon
from fastapi_chameleon import template


router = fastapi.APIRouter()


@router.get("/")
@template()
def index(user: str = "anon"):
    return {"user_name": user}


@router.get("/about")
def about():
    return {}
