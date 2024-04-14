from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    fullname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None
    onboardingpass = models.BooleanField(default=False)
    articles = models.TextField(null=True)
    roadmap = models.TextField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
