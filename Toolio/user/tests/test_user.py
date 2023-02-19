from django.test import TestCase
from django.urls import reverse
from user.models import CustomUser


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse("register")
        self.user = {
            'first_name': 'Navn',
            'last_name': 'Navnesen',
            'username': 'brukernavn',
            "phone_number": '12345678',
            'email': 'navn.navnesen@epostkasse.no',
            'password1': 'Sikkert123',
            'password2': 'Sikkert123',
        }

        self.user_short_password = {
            'first_name': 'Navn',
            'last_name': 'Navnesen',
            'username': 'brukernavn',
            "phone_number": '12345678',
            'email': 'navn.navnesen@epostkasse.no',
            'password1': 'Si',
            'password2': 'Si'
        }
        self.user_unmatching_password = {
            'email': 'testemail@gmail.com',
            'first_name': 'Navn',
            'last_name': 'Navnesen',
            'username': 'brukernavn',
            "phone_number": '12345678',
            'email': 'navn.navnesen@epostkasse.no',
            'password1': 'Sikkert123',
            'password2': 'Sikkert124'
        }

        self.user_invalid_email = {
            'email': 'testemail.gmail.com',
            'first_name': 'Navn',
            'last_name': 'Navnesen',
            'username': 'brukernavn',
            "phone_number": '12345678',
            'email': 'navn.navnesen@epostkasse.no',
            'password1': 'Sikkert123',
            'password2': 'Sikkert124'
        }

        self.user_invalid_number = {
            'email': 'testemail.gmail.com',
            'first_name': 'Navn',
            'last_name': 'Navnesen',
            'username': 'brukernavn',
            "phone_number": 'dddd',
            'email': 'navn.navnesen@epostkasse.no',
            'password1': 'Sikkert123',
            'password2': 'Sikkert124'
        }

        return super().setUp()


class RegisterTest(BaseTest):
    def test_register_page_is_visible(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("user/register.html")

    def test_register_new_user(self):
        response = self.client.post(
            self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_register_new_user_check_database(self):
        self.client.post(
            self.register_url, self.user, format='text/html')

        user_exists = CustomUser.objects.filter(
            username=self.user["username"]).exists()
        self.assertTrue(user_exists, f"User was not created in the database.")

    def test_register_none_existent_in_database(self):
        self.client.post(
            self.register_url, self.user, format='text/html')

        user_exists = CustomUser.objects.filter(
            username="NotAUserName").exists()
        self.assertFalse(user_exists, f"User was not created in the database.")

    def test_cant_register_user_withshortpassword(self):
        response = self.client.post(
            self.register_url, self.user_short_password, format='text/html')
        self.assertEqual(response.status_code, 400)

    def test_cant_register_user_with_unmatching_passwords(self):
        response = self.client.post(
            self.register_url, self.user_unmatching_password, format='text/html')
        self.assertEqual(response.status_code, 400)

    def test_cant_register_user_with_invalid_email(self):
        response = self.client.post(
            self.register_url, self.user_invalid_email, format='text/html')
        self.assertEqual(response.status_code, 400)

    def test_cant_register_user_with_taken_email(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(
            self.register_url, self.user, format='text/html')

        self.assertEqual(response.status_code, 400)

    def test_cant_register_user_with_invalid_number(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(
            self.register_url, self.user_invalid_number, format='text/html')
        self.assertEqual(response.status_code, 400)
