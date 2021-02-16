from django.db import models
from django.db.models import JSONField, DateTimeField


class Answer(models.Model):
    values = JSONField(null=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return str(f'{self.id} {self.values}')
