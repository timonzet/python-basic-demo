from fastapi import APIRouter

router = APIRouter(
    prefix="/ping",
)


@router.get("/")
def get_view():
    return {
        "message": "pong",
    }
