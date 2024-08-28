from django.db import models


def author_image_file_path(instance,filename):
    return '/'.join([str(instance.name),filename])
class Author(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    age=models.IntegerField(null=True)
    image = models.ImageField(upload_to=author_image_file_path,null=True,blank=True)
# Create your models here.
