from django.db import models

# Create your models here.
class UrlDB(models.Model):
    short_url = models.CharField(max_length=250,unique=True)
    resource_url = models.CharField(max_length=1000)