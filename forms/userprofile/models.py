from django.db import models

class Review(models.Model):
    user_name = models.CharField(max_length=20)
    text  = models.TextField()
    rating = models.IntegerField()
# Create your models here.
