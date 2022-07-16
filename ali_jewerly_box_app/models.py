
from contextlib import nullcontext
from sre_parse import CATEGORIES
from django.db import models
from cloudinary.models import CloudinaryField 

# Create your models here.

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    
    )

CATEGORIES = (
    ('ICED WATCH', 'ICED WATCH'),
    ('LEATHER WATCH', 'LEATHER WATCH'),
    ('NECKLACE', 'NECKLACE'),
    ('RINGs', 'RING'),
    ('GRILL', 'GRILL')
    )
    


class Product(models.Model):
    gender = models.CharField(max_length=50, choices=GENDER, default="MALE")
    category = models.CharField(max_length=50, choices=CATEGORIES, default="ICED WATCH", null=True)
    title = models.CharField(max_length=50)
    image =CloudinaryField('image')
    description = models.TextField(max_length=200)
    price = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
