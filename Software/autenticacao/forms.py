from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm

class RegisterForms(UserCreationForm):
    ...