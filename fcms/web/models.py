from django.db import models
from django.contrib.auth.models import User


class Community(models.Model):
    class Meta:
        verbose_name_plural = 'Communities'
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    owner = models.ForeignKey(User)
    created_at = models.DateField(auto_now=True)


class Event(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    geolocalization = models.CharField(max_length=255)
    event_url = models.CharField(max_length=255)
    image_event = models.FileField(upload_to='events/')
    owner_user = models.ForeignKey(User)
    community = models.ForeignKey('Community')


class EventDate(models.Model):
    id_event = models.ForeignKey('Event')
    date = models.DateField()
    time = models.TimeField()
