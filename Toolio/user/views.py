from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

# Create your views here.
def register(response):
  if response.method == "POST":
    form = RegisterForm(response.POST)
    if form.is_valid():
      form.save()
      return redirect("/")
    else:
      # Her skal alert komme HUSK MER HER ANDREAS
      messages.success(response, 'ERROR: Passord er ikke like')
      form = RegisterForm()
      return render(response, "user/register.html", {"form": form})
  else:
    form=RegisterForm()
    
    return render(response, "user/register.html", {"form": form})
  