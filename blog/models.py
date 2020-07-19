from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images')

    def summary(self):
        return self.body[:80]

    def __str__(self):
        return self.title


