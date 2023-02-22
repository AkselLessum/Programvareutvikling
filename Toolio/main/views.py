from .models import ad
from django.shortcuts import render, get_object_or_404, redirect
from .forms import createAdForm, editAdForm, editAdFormWanted
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

def home(request):
    context = {
        'adList': ad.objects.all()
    }
    return render(request, "main/home.html", context)

def userPage(request):
    print(request.user.advertisement)
    return render(request, "main/userPage.html", {})

@login_required(login_url=settings.LOGIN_URL)
def createAd(request):
    if request.method == "POST":
        form = createAdForm(request.POST, request.FILES)

        if form.is_valid():
            type = form.cleaned_data["type"]
            #title = form.cleaned_data["title"]
            #date = form.cleaned_data["date"]
            #price = form.cleaned_data["price"]
            #description = form.cleaned_data["description"]
            #image = form.cleaned_data["image"]
            if(type == "requestAd"):
                isRequest = True
            else:
                isRequest = False
                
            newAd = form.save(commit=False)
            newAd.user = request.user
            newAd.isRequest = isRequest
            newAd.save()
            #newAd = ad(isRequest=isRequest, title=title, date=date, price=price, description=description, image=image)
            #newAd.save()
            #request.user.advertisement.add(newAd)
        
        return redirect("/")

    else:
        form = createAdForm()
    return render(request, "main/createAd.html", {"form":form})



def edit_ad(request, ad_id):
    ad_to_edit = get_object_or_404(ad, id=ad_id)

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
    ad_obj = get_object_or_404(ad, id=ad_id)  # use the model class Ad to retrieve the object
    ad_obj.delete()
    return redirect('home')  # redirect to the home page
