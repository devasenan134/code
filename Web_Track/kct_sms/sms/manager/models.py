from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    place_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.place_name


class SecurityRoutine(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null = True)
    start_time = models.TimeField(null = True)
    end_time = models.TimeField(null = True)
    place = models.ForeignKey(Place, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name.username


class Leave(models.Model):
    from_date = models.DateField(null = True)
    to_date = models.DateField(null = True)
    name = models.ForeignKey(User, on_delete = models.CASCADE)
    reason = models.CharField(max_length=200, null=True, blank = True)

    def __str__(self):
        return self.name.username
