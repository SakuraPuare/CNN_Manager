import datetime

import imagehash
import jwt
from PIL import Image
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from tortoise.fields import ReverseRelation

from schemas.user import UserSchema

secret_key = 'sakurapuare'

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def schema_to_dict(schema) -> dict:
    """
    Convert a Tortoise schema to a dictionary.

    """
    data = {}
    for field in schema._meta.fields:
        field_name = field
        value = getattr(schema, field_name)
        if isinstance(value, ReverseRelation):
            value = [schema_to_dict(i) for i in value.related_objects[-10:]]
        elif isinstance(value, datetime.datetime):
            value = value.timestamp()

        data[field_name] = value
    return data


def generate_bearer_token(data: UserSchema, expires_in: int = 3600) -> str:
    """
    Generate a bearer token.

    Parameters:
    - data: a dictionary with the data to encode in the token.
    - secret_key: a secret key used to encode the token.
    - expires_in: the number of seconds until the token expires.
    """

    to_encode = schema_to_dict(data)
    expire = datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=expires_in)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm="HS256")

    return encoded_jwt


def decode_bearer_token(token: str) -> dict:
    """
    Decode a bearer token.

    Parameters:
    - token: the token to decode.
    - secret_key: the secret key used to encode the token.
    """
    if token.startswith("Bearer "):
        token = token.split(" ")[-1]
    decoded_jwt = jwt.decode(token, secret_key, algorithms=["HS256"])
    return decoded_jwt


def image_hash(img: Image, hash_size: int = 16) -> str:
    return imagehash.dhash(img, hash_size=hash_size).__str__()


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserSchema:
    try:
        decoded_token = decode_bearer_token(token)
    except jwt.exceptions.ExpiredSignatureError as e:
        print(e)
        return None
    return await UserSchema.get(id=decoded_token.get("id"))
