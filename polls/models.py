from django.db import models
from shortuuid.django_fields import ShortUUIDField
from users.models import CustomUser

class Election(models.Model):
    id = ShortUUIDField(unique=True, length=5, max_length=5, alphabet="0123456789", primary_key=True)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __repr__(self):
        return self.name.title()
    
    def __str__(self):
        return self.name.title()

class Candidate(models.Model):
    id = ShortUUIDField(unique=True, length=5, max_length=5, alphabet="0123456789", primary_key=True)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __repr__(self):
        return self.name.title()
    
    def __str__(self):
        return self.name.title()

class Vote(models.Model):
    id = ShortUUIDField(unique=True, length=5, max_length=5, alphabet="0123456789", primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.user.username.title()
    
    def __str__(self):
        return self.candidate.election.name.title()