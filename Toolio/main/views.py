from .models import ad, CustomList, adInList
from user.models import CustomUser, Interaction, Interaction
from django.shortcuts import render, get_object_or_404, redirect
from .forms import createAdForm, editAdForm, editAdFormWanted, confirmBooking, createCustomListForm, confirmBooking
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
    
    interaction = Interaction.objects.update_or_create(
        a=request.user,
        b=ad_instance.user,
    )
    interaction[0].rated_a = False
    interaction[0].rated_b = False
    interaction[0].save()
    
    
    return redirect('home')


def get_user_average_rating(user):
    b=True
    interactions = Interaction.objects.filter(b_id=user.id, rating_b__gt=0).exclude(rating_b__isnull=True)
        
    if interactions.count() == 0:
        interactions = Interaction.objects.filter(a_id=user.id, rating_a__gt=0).exclude(rating_a__isnull=True)
        b=False

    if interactions.count() == 0:
        return None

    if b:
        total_rating = sum(interaction.rating_b for interaction in interactions)

    else:
        total_rating = sum(interaction.rating_a for interaction in interactions)

    return total_rating / interactions.count()


def userPage(request, user_id):
    profile_user = CustomUser.objects.get(id=user_id)
    average_rating = get_user_average_rating(profile_user)
    list_form = createCustomListForm()
    print(f"\n\n average rating: {average_rating} \n\n")
    
    context = {
        'profile_user': profile_user,
        'average_rating': average_rating,
        'form': list_form
    }
    return render(request, 'main/userPage.html', context)

def rate_user(request, user_id):
    rated_user = CustomUser.objects.get(id=user_id) #b
    user = request.user #a
    b = True
    
    # Check if an interaction record exists between the borrower and the lender
    interaction = Interaction.objects.filter(a=user, b=rated_user, rated_b=False).first()
    
    # Retrieve the ad object associated with the booking
    ad_obj = ad.objects.filter(isRented=True, user=rated_user).first()

    if interaction==None:
        interaction = Interaction.objects.filter(b=user, a=rated_user, rated_a=False).first()
        print(interaction)
        ad_obj = ad.objects.filter(isRented=True, user=user).first()
        b = False
  
    if request.method == "POST":
        # Check if the user has confirmed the booking and if an interaction record exists
        if ad_obj and interaction and b:
            rating = int(request.POST["rating"])
            interaction.rating_b = rating
            interaction.rated_b = True
            interaction.save()
            return redirect('userPage', user_id)
        elif ad_obj and interaction:
            rating = int(request.POST["rating"])
            interaction.rating_a = rating
            interaction.rated_a = True
            interaction.save()
            return redirect('userPage', user_id)
        else:
            print("         __")
            print("        / _)")
            print(" .-^^^-/ /")
            print("(_,____/   ")

   
    return redirect('userPage', user_id)

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