from django.db import models
from registration.models import Actor

# Create your models here.


class Film (models.Model):
    filmname = models.CharField(max_length=50)
    dateRelease = models.DateField()
    actorRole = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    actor = models.ManyToManyField(Actor)

