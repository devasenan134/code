from djongo import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    likes = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.title