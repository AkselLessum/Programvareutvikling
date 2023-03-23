from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

from .forms import RegisterForm, LogInForm


# Create your views here.
def register(request):
  form=RegisterForm()
  
  context = {
    "form": form
  }
  
  if request.method == "POST":
    form = RegisterForm(request.POST)

    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("/")
    
    else:
      for field in form:
        if "password" not in field.name:
          context[field.name] = form[field.name].value()
        for error in field.errors:
          messages.error(request, error)
    
      return render(request, "user/register.html", context, status=400)

  return render(request, "user/register.html", context)

def log_in(request):
  form = LogInForm()
  error = False
  
  context = {
    "form": form,
    "error": error
  }
  
  if request.user.is_authenticated:
    return redirect('home')
  if request.method == "POST":
    form = LogInForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data["username"]
      password = form.cleaned_data["password"]
      user = authenticate(username=username, password=password)
      if user:
        login(request, user)
        return redirect("/")
      else:
        context["username"] = username
        messages.info(request, 'Brukernavn eller passord er ugyldig.')
        error = True
    
  return render(request, "user/login.html", context)

def log_out(request):
  logout(request)
  return redirect(reverse("user:login"))