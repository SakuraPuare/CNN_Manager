from tortoise import fields
from tortoise.models import Model


class LogsSchema(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.UserSchema', related_name='logs')
    action = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'logs'
