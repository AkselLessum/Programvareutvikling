from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
  email = forms.EmailField()
  phone_number = forms.IntegerField()
  
  class Meta:
    model = User
    fields = ["first_name","last_name", "username","phone_number", "email", "password1", "password2"]