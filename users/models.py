from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_voter = models.BooleanField(detault=True)
    is_admin = models.BooleanField(default=False)