from tortoise import fields
from tortoise.models import Model


class UserSchema(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, null=True)
    password = fields.CharField(max_length=255, null=True)

    is_admin = fields.BooleanField(null=False, default=False)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'user'

