from django.shortcuts import render

# Create your views here.

def home(url):
    return render(url, 'home.html')
