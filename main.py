from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from rich.traceback import install
from tortoise.contrib.fastapi import register_tortoise

from router import base_router
from schemas import *
from utils import decode_bearer_token, generate_bearer_token

install(show_locals=True)

app = FastAPI()

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
class AuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            request = Request(scope, receive)
            if any(request.url.path.startswith(i) for i in white_list):
                await self.app(scope, receive, send)
                return
            if any(request.url.path.startswith(i) for i in admin_list):
                try:
                    if "Authorization" not in request.headers:
                        raise HTTPException(status_code=401, detail="Token is required")
                    token = request.headers["Authorization"]
                    data = decode_bearer_token(token)
                    user = UserSchema(**data)
                    request.state.user = user
                    if not user.is_admin:
                        raise HTTPException(status_code=401, detail="Permission denied")
                    await self.app(scope, receive, send)
                    return
                except Exception as e:
                    raise HTTPException(status_code=401, detail="Token is invalid")
            await self.app(scope, receive, send)

app.add_middleware(AuthMiddleware)
app.include_router(base_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}



register_tortoise(
    app,
    # memory mode
    # db_url="sqlite://:memory:",
    db_url="mysql://root:123456@localhost:3306/cnn",
    modules={"models": ["schemas"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
