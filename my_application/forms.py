from urllib import request
from django import forms


class Contact_Form(forms.Form):

    name = forms.CharField(max_length=100,required=True)

    email = forms.EmailField(required=True)

    message = forms.CharField(widget=forms.Textarea,required=True)

    