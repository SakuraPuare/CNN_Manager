from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from schemas import *
from models import *
from utils import decode_bearer_token, generate_bearer_token

app = FastAPI()

origins = [
    '*'
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
async def check_user(request: Request, call_next):
    if request.url.path not in white_list:
        if "Authorization" not in request.headers:
            return 401
        token = request.headers["Authorization"]
        try:
            token = token.split('Bearer ')[-1]
            decode = decode_bearer_token(token)
        except Exception as e:
            return 401
        is_admin = decode.get("is_admin")
        if request.url.path in admin_list and not is_admin:
            return 403
        else:
            request.state.user = decode
    response = await call_next(request)
    return response


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/login",response_model=UserOut)
async def login(user: UserIn):
    user_obj = await UserSchema.get(username=user.username)
    if not user_obj or user_obj.password != user.password:
        raise HTTPException(status_code=400, detail="Invalid password")
    token = generate_bearer_token(user_obj)
    user_obj.token = token
    obj = UserOut.from_orm(user_obj)
    return obj


@app.post("/register", response_model=UserOut)
async def register(user: UserIn):
    if await UserSchema.filter(username=user.username).exists():
        raise HTTPException(status_code=400, detail="Username already exists")
    user_obj = await UserSchema.create(**user.dict())
    token = generate_bearer_token(user_obj)
    user_obj.token = token
    obj = UserOut.from_orm(user_obj)
    return obj


register_tortoise(
    app,
    # memory mode
    db_url="sqlite://:memory:",
    # db_url="mysql://root:123456@localhost:3306/cnn",
    modules={"models": ["schemas"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
