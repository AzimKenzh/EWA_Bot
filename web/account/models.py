from django.contrib.auth.models import AbstractUser
from django.db import models


class Status(models.Model):
    title = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.title or ''


class MyUser(AbstractUser):
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, related_name='myusers', blank=True, null=True)
    username = models.CharField(max_length=170, unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

