# from django.forms import ModelForm, ValidationError
# from .models import id13in
from django import forms
from . import id13check
from .models import Image
import logging
import re
import collections
import datetime

import django.forms
import django.forms.utils
import django.forms.widgets
import django.core.validators
import django.core.exceptions
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
# import form_utils.forms
# import requests
# import dateutil.parser
# import validate_email


# first time sign up
class FormEntry(forms.Form):
    ID13 = forms.CharField(max_length=13)  # Thai id number
    confirmed = forms.BooleanField()


# sign in using 13ID and BD
class FormSignIn(forms.Form):
    ID13 = forms.CharField(max_length=13)  # Thai id number
    # birthdate = forms.DateField(label='วันเกิดผู้สมัคร', widget=forms.SelectDateWidget)  # BD
    birthdate = forms.DateField(label='วันเกิดผู้สมัคร', widget=forms.NumberInput(attrs={'type':'date'}))  # BD
    confirmed = forms.BooleanField()


class FormSignIn(forms.Form):
    ID13 = forms.CharField(max_length=13)  # Thai id number
    # birthdate = forms.DateField(label='วันเกิดผู้สมัคร', widget=forms.SelectDateWidget)  # BD
    birthdate = forms.DateField(label='วันเกิดผู้สมัคร', widget=forms.NumberInput(attrs={'type':'date'}))  # BD
    confirmed = forms.BooleanField()


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')