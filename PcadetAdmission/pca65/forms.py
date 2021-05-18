# from django.forms import ModelForm, ValidationError
# from .models import id13in
from django import forms
from . import id13check

class FormName(forms.Form):
    ID13 = forms.CharField(max_length=13)  # Thai id number
    confirmed = forms.BooleanField()
