from .models import ad, CustomList, adInList
from user.models import CustomUser
from django.shortcuts import render, get_object_or_404, redirect
from .forms import createAdForm, editAdForm, editAdFormWanted, createCustomListForm
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

def userPage(request, user_id):
    user_page = get_object_or_404(CustomUser, id=user_id)
    list_form = createCustomListForm()
    #save_form = saveAdToListForm()
    return render(request, 'main/userPage.html', {'ad_user': user_page, 'form': list_form})
    


@login_required(login_url=settings.LOGIN_URL)
def createAd(request):
    if request.method == "POST":
        form = createAdForm(request.POST, request.FILES)
        print(request.POST)     #### why print her

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

def create_custom_list(request, user_id):
    if request.method == "POST":
        form = createCustomListForm(request.POST)

        if form.is_valid():
            newList = form.save(commit=False)
            newList.user = request.user
            newList.save()
        return redirect("/")

    else:
        form = createCustomListForm()
    return redirect('userPage', request.user)

def save_ad_to_list(request, user_id):
    ad_id = request.POST["ad_id"]
    list_id = request.POST["list_id"]
    ad_to_save = ad.objects.get(pk=ad_id)
    list_to_add = CustomList.objects.get(pk=list_id)
    
    saved_ad_to_list, created = adInList.objects.get_or_create(
        customList = list_to_add,
        savedAd = ad_to_save
    )
    print(f'\n Ad: {saved_ad_to_list.savedAd.title} to the list: {saved_ad_to_list.customList.title}\n')
    
    return redirect('userPage', request.user.id)