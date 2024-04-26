from tortoise import fields
from tortoise.models import Model


class NetworkSchema(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    description = fields.TextField()

    network = fields.TextField()
    backend = fields.TextField()
    catalog = fields.TextField()

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'network'
