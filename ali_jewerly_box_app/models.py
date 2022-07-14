
from django.db import models
from cloudinary.models import CloudinaryField 

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    image =CloudinaryField('image')
    description = models.TextField(max_length=200)
    price = models.CharField(max_length=6)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
