from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField()
    url = None
    date = None
    slug = models.SlugField(unique=True, max_length=50)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    cover = models.ImageField(default='default.png', blank=True)


# class Document(models.Model):
#     description = models.CharField(max_length=250, blank=True)
#     document = models.FileField(upload_to='documents/')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

# class User(AbstractUser):
#     pass