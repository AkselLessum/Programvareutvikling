# User

The user application handles user registration and login. The model [CustomUser](models.py) has been made by extending the [AbstractUser](https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model) model. To override the default user model a value for **AUTH_USER_MODEL** is provided in the [settings.py](../Toolio/settings.py) file:

```
AUTH_USER_MODEL = 'user.CustomUser'
```

## Registration

The registration [form](forms.py) for new users has been made by extending the [UserCreationForm](https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.forms.UserCreationForm) from [django.contrib.auth.forms](https://docs.djangoproject.com/en/4.1/topics/auth/default/#module-django.contrib.auth.forms). In [views.py](views.py) the form is validated, and if valid a new user is registered.

## Login and Logout

Login as well as logout is handled by the [django.contrib.auth](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/) backend. Once a user is logged inn the profile button will take them to their [userPage](../main/templates/main/userPage.html).

## Testing

Various tests to ensure the user registration and login features works as expected. The tests are implemented using Django's built-in [testing framework](https://docs.djangoproject.com/en/4.1/topics/testing/overview/), and are located in the tests folder in the users app.

To run all test in the user application run:

```
python ../manage.py test user
```
