from django.http import HttpResponse
from django.shortcuts import render
from .models import Coffe
# Create your views here.

def home(request):
    coffe = Coffe.objects.all()
    return render (request, 'home.html',{'coffe': coffe})
