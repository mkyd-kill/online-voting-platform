from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_voter = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    profile_img = models.ImageField(upload_to='profiles/', blank=True, null=True, default='avatar.jpg')