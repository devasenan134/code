from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    content = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title