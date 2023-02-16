from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username",
                  "email", "password1", "password2"]


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "email"]


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(
        attrs={'class': 'forms-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
