from django.db import models

# Create your models here.


class Job(models.Model):
    images = models.ImageField(upload_to='images')
    summary = models.TextField(max_length=200)

