
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import * 

# Create your views here.
@api_view(['GET', 'POST'])
def products(request):
    if request.method == 'GET':
        prod = Product.objects.all()
        prod_serializ = ProductSerializer(prod, many=True)
        return Response(prod_serializ.data)
    elif request.method == 'POST':
        prod_serializ= ProductSerializer(data = request.data, files = request.FILES)
        if prod_serializ.is_valid():
            prod_serializ.save()
            return Response(prod_serializ.data, status=status.HTTP_201_CREATED)
        return Response(prod_serializ.errors, status=status.HTTP_400_BAD_REQUEST)
    
