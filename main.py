from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
# from rich.traceback import install
from tortoise.contrib.fastapi import register_tortoise
from fastapi.responses import Response
from router import base_router
from utils import get_current_user

# install(show_locals=True)

app = FastAPI()

register_tortoise(
    app,
    # db_url="sqlite://:memory:",
    db_url="mysql://root:123456@localhost:3306/cnn",
    modules={"models": ["schemas"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

# generate schemas


origins = [
    '*',
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

white_list = ["/login", "/register"]
admin_list = ["/admin"]


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    if any(request.url.path.startswith(i) for i in white_list):
        response = await call_next(request)
        return response

    if "Authorization" not in request.headers:
        return Response(status_code=401, content="Token is required")

    token = request.headers.get("Authorization")
    user = await get_current_user(token)
    if user is None:
        return Response(status_code=401, content="Invalid token")

    if any(request.url.path.startswith(i) for i in admin_list):
        if not user.is_admin:
            return Response(status_code=403, content="Permission denied")
    response = await call_next(request)
    return response


app.include_router(base_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
