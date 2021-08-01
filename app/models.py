from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name: str = models.CharField(max_length=30)
    last_name: str = models.CharField(max_length=30)
    image_url: str = models.URLField()


class Book(models.Model):
    title: str = models.CharField(max_length=30)
    description: str = models.TextField()
    image: str = models.URLField()
    type: str = models.CharField(max_length=30)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
