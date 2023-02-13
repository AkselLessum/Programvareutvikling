from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class CustomUser(AbstractUser):
    phone_number = models.IntegerField(unique=True)
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, help_text='The groups this user belongs to.', related_name='user_customuser')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, help_text='Specific permissions for this user.', related_name='user_customuser')


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.IntegerField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "phone_number", "email", "password1", "password2"]

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("This phone number is already in use.")
        return phone_number
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email




  