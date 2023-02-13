from django.test import TestCase
from django.urls import reverse

class createAdTest(TestCase):

    def __init__(self, inp):
        super().__init__(inp)
        self.create_ad_url = reverse("createAd")
#

    def test_create_ad_url_check(self):
        response = self.client.get(self.create_ad_url)
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        self.ad = {}

        return super().setUp()

    def test_create_new_ad(self):
        self.setUp()
        response = self.client.post(
            self.create_ad_url, self.ad, format='text/html')
        self.assertEqual(response.status_code, 200)