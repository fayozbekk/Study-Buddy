from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='avas/', blank=True, null=True)
    bio = models.TextField('Bio', blank=True, null=True)


class Category(models.Model):
    objects = None
    cat_name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.cat_name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = 'Kategoriya'
        ordering = ['cat_name']


class RoomModel(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    participants = models.ManyToManyField(User, related_name='ptns')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class META:
        ordering = ['-updated', '-created']

    # Create your models here.
    def __str__(self) -> str:
        return self.title


class Message(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(RoomModel, on_delete=models.CASCADE)
    message = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message[0:50]
