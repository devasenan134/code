from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Score(models.Model):
    source_file = models.FileField(name='source_file', upload_to='home/files')
    description = models.CharField(max_length=300)