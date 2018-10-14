from django.db import models


class Appointment(models.Model):

    name = models.CharField(max_length=30)
    date = models.DateField(auto_now=True)
    notes = models.CharField(max_length=200)
    age = models.IntegerField()
    secrets = models.CharField(max_length=100)