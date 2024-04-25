from tortoise import fields
from tortoise.models import Model


class ImageSchema(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.UserSchema', related_name='images')
    name = fields.CharField(max_length=255, null=True)
    description = fields.TextField(null=True)
    image_hash = fields.CharField(max_length=255, null=True)
    height = fields.IntField()
    width = fields.IntField()
    file_size = fields.IntField()
    type = fields.CharField(max_length=10, null=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'image'
