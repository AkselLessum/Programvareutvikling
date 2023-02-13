from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    def test_testhomepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)