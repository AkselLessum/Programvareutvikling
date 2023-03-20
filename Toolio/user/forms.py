from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from .models import CustomUser


class RegisterForm(UserCreationForm):
    # define phone_number field
    phone_number = forms.IntegerField(required=True)
    # define postal_code field with custom validator
    postal_code = forms.CharField(
        max_length=4,
        validators=[RegexValidator(
            r'^\d{4}$', 'Postal code must be 4 digits.')],
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "username", "phone_number",
                  "postal_code", "email", "password1", "password2"]

    def clean_phone_number(self):
        # get phone_number value from cleaned_data dict, and check if it already exists in database
        phone_number = self.cleaned_data.get('phone_number')
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("This phone number is already in use.")
        return phone_number

    def clean_email(self):
        # get email value from cleaned_data dict, and check if it already exists in database
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("This email is already in use.")
        return email


class LogInForm(forms.Form):
    # define username field
    username = forms.CharField()
    # define password field with widget set to PasswordInput for masking password
    password = forms.CharField(widget=forms.PasswordInput)
