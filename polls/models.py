from django.db import models
from shortuuid.django_fields import ShortUUIDField
from users.models import CustomUser

class Election(models.Model):
    id = ShortUUIDField(unique=True, max_length=5, alphabet="0123456789", primary_key=True)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

class Candidate(models.Model):
    id = ShortUUIDField(unique=True, max_length=5, alphabet="0123456789", primary_key=True)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class Vote(models.Model):
    id = ShortUUIDField(unique=True, max_length=5, alphabet="0123456789", primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)