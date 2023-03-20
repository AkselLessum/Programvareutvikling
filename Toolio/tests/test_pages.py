
from django.test import Client, TestCase
from django.urls import reverse

class MainUrlsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_url(self):
        url = reverse("home")
        response = self.client.get(url)
        status_code = response.status_code
        print("Asserting that the homepage loads...")
        self.assertTrue(
            status_code == 200, msg=f"TEST FAILED: The URL {url} returned a {response.status_code} status code.")
