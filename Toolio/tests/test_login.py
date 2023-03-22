from django.test import TestCase, Client
from user.models import CustomUser
from django.urls import reverse


class LogInTest(TestCase):
    # sets up the conditions necessary to test the login
    def setUp(self):
        self.login_url = reverse('user:login')

        self.credentials = {
            'username': 'brukernavn',
            'password': 'user',
            "phone_number": '12345678'}

        # creates a User objects with the specified credentials
        CustomUser.objects.create_user(**self.credentials)

    def test_invalidLogin_username(self):
        # makes a post request log log in an invalid username
        wrong_username_credentials = self.credentials
        wrong_username_credentials['username'] = 'wrong'
        response = self.client.post(
            self.login_url, wrong_username_credentials, follow=True)

        # checks that the invalid user is not authenticated
        print("Asserts that a user with the wrong username is not authenticated ...")
        self.assertFalse(response.context['user'].is_authenticated)

    def test_invalidLogin_password(self):
        # makes a post request log log in an invalid password
        wrong_password_credentials = self.credentials
        wrong_password_credentials['password'] = 'wrong'
        response = self.client.post(
            self.login_url, wrong_password_credentials, follow=True)

        # checks that the invalid user is not authenticated
        print("Asserts that a user with the wrong password is not authenticated ...")
        self.assertFalse(response.context['user'].is_authenticated)

    def test_validLogin(self):
        # makes a post request to log in a valid user
        response = self.client.post(
            self.login_url, self.credentials, follow=True)

        print("Asserts that the response code of a valid login is correct ...")
        self.assertEquals(response.status_code, 200)

        print("Asserts that a user with valid credentials is authenticated ...")
        self.assertTrue(response.context['user'].is_authenticated)
