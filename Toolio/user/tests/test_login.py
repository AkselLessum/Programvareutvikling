from django.test import TestCase, Client
from django.contrib.auth.models import User


class LogInTest(TestCase):
    # sets up the conditions necessary to test the login
    def setUp(self):
        self.credentials = {
            'username': 'test',
            'password': 'user'}

        # creates a User objects with the specified credentials
        User.objects.create_user(**self.credentials)

    def test_invalidLogin(self):
        # makes a post request log log in an invalid user
        response = self.client.post('/login/', {'username': 'wrong',
                                                'password': 'wrongpassword'}, follow=True)

        # checks that the invalid user is not authenticated
        self.assertFalse(response.context['user'].is_authenticated)

    def test_validLogin(self):
        # makes a post request to log in a valid user
        response = self.client.post('/login/', self.credentials, follow=True)

        # checks that status code of response is as intended (200)
        self.assertEquals(response.status_code, 200)

        # checks that the user is authenticated
        self.assertTrue(response.context['user'].is_authenticated)
