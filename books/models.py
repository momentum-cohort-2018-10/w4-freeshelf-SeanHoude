from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.
class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Book(Timestamp):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=30, blank=True, null=True)
    series = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=50)
    creator = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    cover = models.ImageField(default='default.png', blank=True)
    favorited = models.IntegerField(default=0)
    is_fantasy = models.BooleanField(default=False)
    is_scifi = models.BooleanField(default=False)
    is_horror = models.BooleanField(default=False)

    def get_absolute_url(self):
        return "books/%s/" % self.slug

class Comment(Timestamp):
    username = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT, null=True)
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    liked = models.IntegerField(default=0)

def get_image_path(instance, filename):
    return '/'.join(['book_images', instance.book.slug, filename])

class Upload(Timestamp):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="uploads")
    image = models.ImageField(upload_to=get_image_path)

# class Social(models.Model):
#     SOCIAL_TYPES = (
#         ('twitter', 'Twitter'),
#         ('facebook', 'Facebook'),
#         ('pinterest', 'Pinterest'),
#         ('instagram', 'Instagram'),
#         ('linkedin', 'LinkedIn')
#     )
#     network = models.CharField(max_length=250, choices=SOCIAL_TYPES)
#     username = models.CharField(max_length=50)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="social_accounts")

#     class Meta:
#         verbose_name_plural = "Social media links"
