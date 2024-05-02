from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
# from rich.traceback import install
from tortoise.contrib.fastapi import register_tortoise

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

white_list = ["/login", "/register", "/image/file"]
admin_list = ["/admin"]


@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    print([request.url.path.startswith(i) for i in white_list])
    if request.method == "OPTIONS" or any(request.url.path.startswith(i) for i in white_list):
        response = await call_next(request)
        return response

    if "Authorization" not in request.headers:
        return JSONResponse(status_code=401, content={"detail": "Authorization required"})

    token = request.headers.get("Authorization")
    user = await get_current_user(token)
    if user is None:
        return JSONResponse(status_code=401, content={"detail": "Invalid token"})

    if any(request.url.path.startswith(i) for i in admin_list):
        if not user.is_admin:
            return JSONResponse(status_code=403, content={"detail": "Permission denied"})
    response = await call_next(request)
    return response


app.include_router(base_router)


@app.get("/")
async def root():
    return {"detail": "Hello World"}
