from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from main.models import ad
from user.models import CustomUser


class AdViewsTestCase(TestCase):

    def setUp(self):
        self.ad_url = reverse('createAd')
        self.credentials = {
            'username': 'brukernavn',
            'password': 'Bananmann1',
            "phone_number": '12345678'}
        # creates a User objects with the specified credentials
        CustomUser.objects.create_user(**self.credentials)
        bruker = CustomUser.objects.get(username="brukernavn")
        
        self.ad_data = {
            "user": bruker,
            "isRequest": False,
            "isRented": False,
            "title": "Test Ad",
            "category": "Test Category",
            "date": "2023-03-15",
            "price": 100,
            "description": "Test Description",
            "image": SimpleUploadedFile("test_image.png", b"file_content", content_type="image/png")
        }
        self.ad_data_request = {
            "user": bruker,
            "isRequest": True,
            "isRented": False,
            "title": "Test Ad",
            "category": "Test Category",
            "date": "2023-03-15",
            "price": 100,
            "description": "Test Description",
            "image": SimpleUploadedFile("test_image.png", b"file_content", content_type="image/png")
        }
        self.invalid_ad_data = {
            "user": bruker,
            "isRequest": False,
            "isRented": False,
            "title": "",  # title is required
            "category": "Test Category",
            "date": "2023-03-15",
            "price": 100,
            "description": "Test Description",
            "image": SimpleUploadedFile("test_image.png", b"file_content", content_type="image/png")
        }
        self.ad = ad.objects.create(**self.ad_data)

    def test_create_ad(self):
        self.client.login(username="brukernavn", password="Bananmann1")
        response = self.client.post(
            self.ad_url, data=self.ad_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ad.objects.filter(title="Test Ad").exists(), msg="FAILED: ad was not created")

    
    def test_create_request_ad(self):
        self.client.login(username="brukernavn", password="Bananmann1")
        response = self.client.post(
            self.ad_url, data=self.ad_data_request, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ad.objects.filter(title="Test Ad").exists(), msg="FAILED: ad was not created")    

    def test_create_invalid_ad(self):
        self.client.login(username="brukernavn", password="Bananmann1")
        response = self.client.post(
            self.ad_url, data=self.invalid_ad_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(ad.objects.filter(title="").exists(), msg="FAILED: able to create ad without title")

""" def test_access_ad(self):
        response = self.client.get(
            reverse("ad_detail", kwargs={"pk": self.ad.id}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Ad")"""
