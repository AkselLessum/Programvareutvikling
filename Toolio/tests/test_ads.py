from django.test import TestCase, Client
from user.models import CustomUser
from django.urls import reverse

class AdTest(TestCase):
    #Creates a User that will create the ads.
    def setUp(self):
        self.credentials = {
            'username': 'Ad_Test_User',
            'password': 'Bananmann1',
            "phone_number": '12345676',
            'postal_code': '4022',
            'email':'ad_test@gmail.com'}

        # creates a User object with the specified credentials
        CustomUser.objects.create_user(**self.credentials)
    fields = ["first_name", "last_name", "username", "phone_number", "postal_code", "email", "password1", "password2"]
    
