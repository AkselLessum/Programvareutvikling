from django.shortcuts import render, redirect
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
            image = form.cleaned_data["image"]
            if(type == "requestAd"):
                request = True
            else:
                request = False
            newAd = ad(isRequest=request, title=title, date=date, price=price, description=description, image=image)
            newAd.save()
        
        return redirect("/")

    else:
        form = createAdForm()
    return render(response, "main/createAd.html", {"form":form})

def popup_view(request):
    return render(request, 'popup.html')