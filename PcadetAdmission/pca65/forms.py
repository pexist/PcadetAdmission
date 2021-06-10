# from django.forms import ModelForm, ValidationError
# from .models import id13in
from django import forms
from . import id13check
from .models import Image

class FormName(forms.Form):
    ID13 = forms.CharField(max_length=13)  # Thai id number
    confirmed = forms.BooleanField()



class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')