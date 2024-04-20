import jwt
import datetime

# from tortoise import fields

from schemas import UserSchema

secret_key = 'sakurapuare'


def schema_to_dict(schema) -> dict:
    """
    Convert a Tortoise schema to a dictionary.

    """
    data = {}
    for field in schema._meta.fields:
        field_name = field
        value = getattr(schema, field_name)
        # if isinstance(field, fields.ForeignKeyField):
        #     if value:
        #         value = value.id
        #     else:
        #         value = None

        if isinstance(value, datetime.datetime):
            value = value.isoformat()

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
    expire = datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_in)
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

    decoded_jwt = jwt.decode(token, secret_key, algorithms=["HS256"])

    return decoded_jwt
