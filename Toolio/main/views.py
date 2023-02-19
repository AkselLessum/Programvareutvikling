from .models import Ad
from django.shortcuts import render, get_object_or_404, redirect
from .forms import createAdForm, editAdForm, editAdFormWanted
# Create your views here.

def home(response):
    context = {
        'adList': Ad.objects.all()
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
            newAd = Ad(isRequest=request, title=title, date=date, price=price, description=description, image=image)
            newAd.save()
        
        return redirect("/")

    else:
        form = createAdForm()
    return render(response, "main/createAd.html", {"form":form})



def edit_ad(request, ad_id):
    ad_to_edit = get_object_or_404(Ad, id=ad_id)

    if ad_to_edit.isRequest: # Different classes for editing "annonse" and editing "ønskes leid"
        form_class = editAdFormWanted
    else:
        form_class = editAdForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=ad_to_edit)
        if form.is_valid():
            ad_obj = form.save(commit=True)
            return redirect('/')
    else:
        form = form_class(instance=ad_to_edit)
    return render(request, 'main/editAd.html', {'form': form, 'ad': ad_to_edit})



def delete_ad(request, ad_id):
    ad = get_object_or_404(Ad, pk=ad_id)  # use the model class Ad to retrieve the object
    ad.delete()
    return redirect('home')  # redirect to the home page
