from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    url = models.URLField()
    img = models.ImageField(upload_to="home/thumbnails/")
    date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return self.title
