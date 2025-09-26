from math import e
import re
from django.http import HttpResponse
from django.shortcuts import render
from .models import Sample_data
from .forms import Contact_Form

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



def regroup_jinja(request):

    books = [
        {"title": "Python Basics", "category": "Programming"},
        {"title": "Django Mastery", "category": "Programming"},
        {"title": "React Guide", "category": "Web Development"},
        {"title": "HTML & CSS", "category": "Web Development"},
        {"title": "Data Science 101", "category": "Data Science"},
    ]

    return render(request,"regroup.html",{"Books" : books})


def html_form(request):

    if request.method == "POST":

        print("-------- Request ------",request)

        print("-------- Method -------",request.method)

        print("-------- Username -------",request.POST.get("username"))
        print("-------- Password -------",request.POST.get("password"))

        user_name = request.POST.get("username")
        pass_word = request.POST.get("password")

        if user_name == "admin" and pass_word == "1234":

            return render(request,"Login_success.html",{"user" : user_name})
        
        else:

            return render(request,"login.html",{"Error" : "Invalid Credentials"})

    return render(request,"login.html")




def django_normal_form(request):

    C_form = Contact_Form()

    if request.method == "POST":

        form = Contact_Form(request.POST)

        print(form)


        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            return HttpResponse(f"Message Received")
        
        else:

            return HttpResponse("Invalid Data")

    return render(request,"contact.html",{"form":C_form})