from .models import ad
from user.models import CustomUser
from django.shortcuts import render, get_object_or_404, redirect
from .forms import createAdForm, editAdForm, editAdFormWanted, confirmBooking
from django.contrib.auth.decorators import login_required
from django.conf import settings
from user.find_distance import get_ad_distance_dict

# Create your views here.

def home(request):
    context = {
        'adList': ad.objects.all()
    }
    
    if request.user.is_authenticated:
        ad_distance_dict = get_ad_distance_dict(request.user)
        context['ad_distance_dict'] = ad_distance_dict
    
        

    return render(request, "main/home.html", context)


def confirm_booking(request, ad_id):
    ad_instance= get_object_or_404(ad, id=ad_id)
    ad_instance.isRented = True
    ad_instance.save()
    
    return redirect('home')



def confirm_booking2(request, ad_id):
    ad_instance= get_object_or_404(ad, id=ad_id)
    #print("pikk:",ad_instance.isRented)
    ad_instance=ad(isRequest=ad_instance.isRequest, title=ad_instance.title, date=ad_instance.date, price=ad_instance.price, description=ad_instance.description, image=ad_instance.image, isRented=True, user_id=ad_instance.user_id)#kategori
    ad_instance.save()
    print("HER BRO:",ad_instance.isRented)
    
    #if request.method == "POST":
    #    form = confirmBooking(request.POST, ad_instance)
    #    print(form)
    #    
    #    if form.is_valid():
    #        form.save(commit=True)
    #        return redirect('/')            
    #
    #else:
    #    form = confirmBooking(instance=ad_instance)
    return render(request, 'main/home.html')
    

def userPage(request, user_id):
    user_page = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'main/userPage.html', {'ad_user': user_page})
    


@login_required(login_url=settings.LOGIN_URL)
def createAd(request):
    if request.method == "POST":
        form = createAdForm(request.POST, request.FILES)
        print(request.POST)

        if form.is_valid():
            type = form.cleaned_data["type"]
            #title = form.cleaned_data["title"]
            #date = form.cleaned_data["date"]
            #price = form.cleaned_data["price"]
            #description = form.cleaned_data["description"]
            #image = form.cleaned_data["image"]
            if (type == "requestAd"):
                isRequest = True
            else:
                isRequest = False

            newAd = form.save(commit=False)
            newAd.user = request.user

            newAd.isRequest = isRequest
            newAd.save()
            #newAd = ad(isRequest=isRequest, title=title, date=date, price=price, description=description, image=image)
            # newAd.save()
            # request.user.advertisement.add(newAd)

        return redirect("/")

    else:
        form = createAdForm()
    return render(request, "main/createAd.html", {"form": form})


def edit_ad(request, ad_id):
    ad_to_edit = get_object_or_404(ad, id=ad_id)

    if ad_to_edit.isRequest:  # Different classes for editing "annonse" and editing "ønskes leid"
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
    # use the model class Ad to retrieve the object
    ad_obj = get_object_or_404(ad, id=ad_id)
    ad_obj.delete()
    return redirect('home')  # redirect to the home page



