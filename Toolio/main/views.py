from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ad
from .forms import createAdForm
# Create your views here.

def home(response):
    context = {
        'adList': ad.objects.all()
    }

    return render(response, "main/home.html", context)

def createAd(response):
    if response.method == "POST":
        form = createAdForm(response.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            date = form.cleaned_data["date"]
            price = form.cleaned_data["price"]
            description = form.cleaned_data["description"]
            # Need to add for image as well
            newAd = ad(title=title, date=date, price=price, description=description)
            newAd.save()
        
        return render(response, "main/home.html", {})

    else:
        form = createAdForm()
    return render(response, "main/createAd.html", {"form":form})