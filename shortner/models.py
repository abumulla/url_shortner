import uuid
from django.db import models

# Create your models here.
class UrlDB(models.Model):
    short_id = models.CharField(max_length=100, editable=False, unique=True, db_index=True)
    resource_url = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.short_id} -> {self.resource_url}"