from django.db import models
from author.models import Author
from django.core.validators import MaxValueValidator,MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=30)
    rating = models.IntegerField(
        validators = [MaxValueValidator(5),MinValueValidator(1)]
    )
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
 
    def __str__(self):
        return self.title