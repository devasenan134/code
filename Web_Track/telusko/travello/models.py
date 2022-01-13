from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="travello/images/")
    desc = models.TextField()
    price = models.IntegerField(blank=False)
    offer = models.BooleanField(default=False)