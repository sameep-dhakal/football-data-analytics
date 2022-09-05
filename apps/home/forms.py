from pickle import FALSE
from django import forms
from django.contrib.auth import get_user_model
from django.forms import ModelForm, widgets

from .models import *

class PlayerDetailsForm(forms.ModelForm):
    
    class Meta:
        model = PlayerDetailsModel
        fields = "__all__"
