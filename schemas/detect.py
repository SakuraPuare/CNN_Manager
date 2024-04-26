from tortoise import fields
from tortoise.models import Model


class DetectSchema(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.UserSchema', related_name='detections')
    image = fields.ForeignKeyField('models.ImageSchema', related_name='detections')
    network = fields.ForeignKeyField('models.NetworkSchema', related_name='detections')
    output = fields.IntField()
    confidence = fields.FloatField()

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'detect'


class FeedbackSchema(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.UserSchema', related_name='feedbacks')
    detect = fields.ForeignKeyField('models.DetectSchema', related_name='feedbacks')
    feedback = fields.IntField()

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = 'feedback'
