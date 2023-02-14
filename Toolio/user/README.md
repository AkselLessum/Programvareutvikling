# User

This part of the code handles user registration and login.

## Registration

The registration [form](forms.py) for new users has been made by extending the [UserCreationForm](https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.forms.UserCreationForm) from [django.contrib.auth.forms](https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.forms). The [frontend](templates/user/register.html) is handled by [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms). In [views.py](views.py) the form is validated, and if valid a new user is registered.

## Login

## Testing