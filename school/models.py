from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    city=models.TextField()
    state=models.TextField()