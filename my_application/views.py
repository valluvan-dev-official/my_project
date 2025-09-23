from django.shortcuts import render
from .models import Sample_data

# Create your views here.


def home(request):

    return render(request,"index.html")


def display(request):

    data = Sample_data.objects.all()

    return render(request,"display.html",{"datas":data})

