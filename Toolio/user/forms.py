from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    phone_number = forms.IntegerField(label="Telefon nummer")
    first_name = forms.CharField(label="Fornavn")
    last_name = forms.CharField(label="Etternavn")
    username = forms.CharField(label="Brukernavn")
    password1 = forms.CharField(label="Passord",widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

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




  