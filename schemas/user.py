from tortoise import fields
from tortoise.models import Model


class UserSchema(Model):
    """
    Represents a user in the system.

    Attributes:
        id (IntField): The unique identifier for the user.
        username (CharField): The username of the user.
        email (CharField): The email address of the user.
        password (CharField): The password of the user.
        is_admin (BooleanField): Indicates whether the user is an admin or not.
        created_at (DatetimeField): The timestamp when the user was created.
        updated_at (DatetimeField): The timestamp when the user was last updated.
    """

    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, null=True)
    email = fields.CharField(max_length=255, null=True)
    password = fields.CharField(max_length=255, null=True)

    is_admin = fields.BooleanField(null=False, default=False)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'user'
