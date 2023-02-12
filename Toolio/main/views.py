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
        form = createAdForm(response.POST, response.FILES)

        if form.is_valid():
            type = form.cleaned_data["type"]
            title = form.cleaned_data["title"]
            date = form.cleaned_data["date"]
            price = form.cleaned_data["price"]
            description = form.cleaned_data["description"]
            adImage = form.cleaned_data["adImage"]
            # Need to add for image as well
            if(type == "requestAd"):
                request = True
            else:
                request = False
            newAd = ad(isRequest=request, title=title, date=date, price=price, description=description, image=adImage)
            newAd.save()
        
        return render(response, "main/home.html", {})

    else:
        form = createAdForm()
    return render(response, "main/createAd.html", {"form":form})