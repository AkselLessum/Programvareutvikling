from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse

from .forms import RegisterForm, LogInForm


# Create your views here.
def register(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)

    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect("/")
    
    else:
      for field in form:
        for error in field.errors:
          messages.error(request, error)
    
      return render(request, "user/register.html", {"form": form}, status=400)

  else:
    form=RegisterForm()

    return render(request, "user/register.html", {"form": form})

def log_in(request):
  error = False
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
        error = True
  else:
    form = LogInForm()
  
  return render(request, "user/login.html", {"form": form, "error": error})

def log_out(request):
  logout(request)
  #return redirect(reverse("user:login"))
  return redirect("/")
  

  