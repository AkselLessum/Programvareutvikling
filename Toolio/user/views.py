from django.shortcuts import render, redirect, get_object_or_404
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

      for field in form:
        for error in field.errors:
          messages.error(response, error)
    
      return render(response, "user/register.html", {"form": form}, status=400) # Gir alt vissuelt, men ikke feilmelding 400
      #return JsonResponse({'errors': form.errors}, status=400) # Gir feilmelding 400, men redirecter til en dumfane
  else:
    form=RegisterForm()

    return render(response, "user/register.html", {"form": form})


