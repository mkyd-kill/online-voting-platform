from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.contrib.auth.models import User

class Election(models.Model):
    id = ShortUUIDField(unique=True, max_length=5, alphabet="0123456789")
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Candidate(models.Model):
    id = ShortUUIDField(unique=True, max_length=5, alphabet="0123456789")
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Vote(models.Model):
    id = ShortUUIDField(unique=True, max_length=5, alphabet="0123456789")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)