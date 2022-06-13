from tortoise import fields, models

__all__ = (
    "User",
    "Evaluation"
)


class User(models.Model):
    user_id = fields.BigIntField(index=True, unique=True)
    username = fields.CharField(32, unique=True, index=True, null=True)
    first_name = fields.CharField(255, null=True)
    last_name = fields.CharField(255, null=True)
    language = fields.CharField(32, default="ru")
    evaluation: "Evaluation"

class Evaluation(models.Model):
    point = fields.IntField()
    user: User = fields.OneToOneField("models.User")
