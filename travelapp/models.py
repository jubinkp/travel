from django.db import models

# Create your models here.

class Place(models.Model):
    name=models.TextField(max_length=250)
    img=models.ImageField(upload_to='pics')

    desc=models.TextField()