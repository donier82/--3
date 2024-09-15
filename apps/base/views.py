from django.shortcuts import render
from django.http import HttpResponse
from .models import About

# Create your views here.
def index(request):
    about=About.objects.latest('id')
    return render(request,'index.html', locals())