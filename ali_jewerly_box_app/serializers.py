from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model: Product
        fields = ['__ all___']
