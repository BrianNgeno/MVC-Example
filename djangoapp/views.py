from django.shortcuts import render
import requests
from .models import HomeInfo

# Create your views here.
def index(request):
    info = HomeInfo.objects.all()
    return (render(request,'index.html', locals()))