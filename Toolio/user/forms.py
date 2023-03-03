from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import CustomUser

class RegisterForm(UserCreationForm):
    phone_number = forms.IntegerField(required=True)
    postal_code = forms.CharField(max_length=4, validators=[RegexValidator(r'^\d{4}$', 'Postal code must be 4 digits.')], required=True)
    
    
    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "phone_number", "postal_code", "email", "password1", "password2"]

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

class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
