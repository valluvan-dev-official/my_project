from django.shortcuts import render
from .models import Sample_data

# Create your views here.


def home(request):

    return render(request,"index.html")


def display(request):

    data = Sample_data.objects.all()

    return render(request,"display.html",{"datas":data})



def Jinja_view(request):

    fruits = ["apple","Orange","MAngo","Banana"]

    return render(request, "jinja.html",{"name":"Hari","age":23,"snakcs" : fruits})


def extends_view(request):


    return render(request,"home.html")
