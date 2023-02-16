from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

from .forms import UpdateUserForm, UpdateProfileForm
from django.contrib import messages
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.models import User


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

            # Gir alt vissuelt, men ikke feilmelding 400
            return render(response, "user/register.html", {"form": form}, status=400)
            # return JsonResponse({'errors': form.errors}, status=400) # Gir feilmelding 400, men redirecter til en dumfane
    else:
        form = RegisterForm()

        return render(response, "user/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(
            request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile updated successfully")
            return redirect(to='/profile')

    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'user/profile.html', {'user_form': user_form, 'profile_form': profile_form})
