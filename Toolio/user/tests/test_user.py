from django.test import TestCase
from django.urls import reverse

class BaseTest(TestCase):
  def setUp(self):
    self.register_url=reverse("register")
    self.user = {
      'first_name': 'Navn',
      'last_name': 'Navnesen',
      'username': 'brukernavn',
      'email': 'navn.navnesen@epostkasse.no',
      'password1': 'Sikkert123',
      'password2': 'Sikkert123'
    }
    
    return super().setUp()

class RegisterTest(BaseTest):
  def test_register_page_is_visible(self):
    response=self.client.get(self.register_url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed("user/register.html")
    
  def test_register_new_user(self):
    response=self.client.post(self.register_url, self.user, format='text/html')
    self.assertEqual(response.status_code, 302)
    