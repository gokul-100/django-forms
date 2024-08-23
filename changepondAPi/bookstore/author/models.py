from django.db import models

class Author(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
# Create your models here.
