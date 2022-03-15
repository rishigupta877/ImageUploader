from distutils.command.upload import upload
from django.db import models

# Create your models here.
class image(models.Model):
    photo=models.ImageField(upload_to='pics')
    date=models.DateTimeField(auto_now_add=True)