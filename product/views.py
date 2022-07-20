from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

# Create your views here.


def index(request):
    context = {'message': 'products'}
    return render(request, 'product/index.html', context)  
    