from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    is_subscribed = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Article(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    paid_content = models.BooleanField(default=False)
