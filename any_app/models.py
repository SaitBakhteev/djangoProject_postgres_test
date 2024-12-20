from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

class Any(models.Model):
    name = ArrayField (models.CharField(max_length=25), size=8)
    age = JSONField (blank=False, null=True)
# Create your models here.
