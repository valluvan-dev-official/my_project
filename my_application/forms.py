from urllib import request
from django import forms
from .models import Student


class Contact_Form(forms.Form):

    name = forms.CharField(max_length=100,required=True)

    email = forms.EmailField(required=True)

    message = forms.CharField(widget=forms.Textarea,required=True)

    

class Student_Form(forms.ModelForm):

    class Meta:
        
        model = Student 
        fields = ["name","age","email"]