from django.contrib.auth.models import AbstractUser
from django.db import models

class Direction(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    level = models.IntegerField(default=1)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username
