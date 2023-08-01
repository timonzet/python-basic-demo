import uvicorn
from fastapi import FastAPI
from view import router as view_router
from items_views import router as items_router
from users.views import router as user_router

app = FastAPI()
app.include_router(
    items_router,
    tags=["Items"],
)
app.include_router(user_router, prefix="/users")
app.include_router(view_router)


@app.get("/")
def index():
    return {
        "message": "Index!",
    }


@app.get("/hello")
def hello(name: str = "World"):
    return {
        "message": f"Hello, {name}!",
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
