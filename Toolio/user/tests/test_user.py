from django.test import TestCase
from django.urls import reverse
from user.models import CustomUser


class BaseTest(TestCase):
    # Create different user profiles to use in tests with and without mistakes.
    def setUp(self):
        # Create the URL for user registration page
        self.register_url = reverse('user:register')

        # A valid user profile
        self.user = {
            'first_name': 'Navn',
            'last_name': 'Navnesen',
            'username': 'brukernavn',
            "phone_number": '12345678',
            'postal_code': '4022',
            'email': 'navn.navnesen@epostkasse.no',
            'password1': 'Sikkert123',
            'password2': 'Sikkert123',
        }

        # A user profile with a duplicate username
        self.user_duplicate_username = {
            'first_name': 'Navn_new',
            'last_name': 'Navnesen_new',
            'username': 'brukernavn',
            "phone_number": '11111111',
            'postal_code': '4022',
            'email': 'navn.navnesen2@epostkasse.no',
            'password1': 'Sikkert123',
            'password2': 'Sikkert123',
        }

        # A user profile with a duplicate email address
        self.user_duplicate_email = {
            'first_name': 'Navn_new',
            'last_name': 'Navnesen_new',
            'username': 'brukernavn_new',
            "phone_number": '22222222',
            'postal_code': '4022',
            'email': 'navn.navnesen2@epostkasse.no',
            'password1': 'Sikkert123',
            'password2': 'Sikkert123',
        }

        # A user profile with a duplicate phone number
        self.user_duplicate_phone = {
            'first_name': 'Navn_new',
            'last_name': 'Navnesen_new',
            'username': 'brukernavn_new2',
            "phone_number": '22222222',
            'postal_code': '4022',
            'email': 'navn.navnesen4@epostkasse.no',
            'password1': 'Sikkert123',
            'password2': 'Sikkert123',
        }

        # A user profile with a short password
        self.user_short_password = {
            'first_name': 'Navn',
            'last_name': 'Navnesen',
            'username': 'brukernavn_new3',
            "phone_number": '44444444',
            'postal_code': '4022',
            'email': 'navn.navnesen5@epostkasse.no',
            'password1': 'Si',
            'password2': 'Si'
        }

        # A user profile with unmatching passwords
        self.user_unmatching_password = {
            'first_name': 'Navn',
            'last_name': 'Navnesen',
            'username': 'brukernavn_new4',
            "phone_number": '55555555',
            'postal_code': '4022',
            'email': 'navn.navnesen6@epostkasse.no',
            'password1': 'Sikkert123',
            'password2': 'Sikkert124'
        }

        # A user profile with an invalid email address
        self.user_invalid_email = {
            'first_name': 'Navn',
            'last_name': 'Navnesen',
            'username': 'brukernavn_new5',
            "phone_number": '66666666',
            'postal_code': '4022',
            'email': 'testemail.gmail.com',
            'password1': 'Sikkert123',
            'password2': 'Sikkert124'
        }

        # A user profile with an invalid phone number
        self.user_invalid_number = {
            'first_name': 'Navn',
            'last_name': 'Navnesen',
            'username': 'brukernavn_new6',
            "phone_number": 'dddd',
            'postal_code': '4022',
            'email': 'navn.navnesen7@epostkasse.no',
            'password1': 'Sikkert123',
            'password2': 'Sikkert123'
        }

        #A user profile with a non existing postal code
        self.user_invalid_postal_code = {
            'first_name': 'Navn',
            'last_name': 'Navnesen',
            'username': 'brukernavn_new7',
            "phone_number": '77777777',
            'postal_code': '40222',
            'email': 'navn.navnesen8@epostkasse.no',
            'password1': 'Sikkert123',
            'password2': 'Sikkert123'
        }


        return super().setUp()


class RegisterTest(BaseTest):
    # Different tests that checks if page loads, if user is created, if user is created in database, if user can register with verious invalid credentials
    def test_register_page_is_visible(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("user/register.html")

    # Checks if the user is able to register.
    def test_register_new_user(self):
        response = self.client.post(
            self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302)

    # Checks if the user is created and exists in the database.
    def test_register_new_user_check_database(self):
        self.client.post(
            self.register_url, self.user, format='text/html')

        user_exists = CustomUser.objects.filter(
            username=self.user["username"]).exists()
        self.assertTrue(user_exists, f"User was not created in the database.")

    # Checks if the user with an invalid username is not created in the database.
    def test_register_none_existent_in_database(self):
        self.client.post(
            self.register_url, self.user, format='text/html')

        user_exists = CustomUser.objects.filter(
            username="NotAUserName").exists()
        self.assertFalse(user_exists, f"User was not created in the database.")

    # Checks if the user is not created when a duplicate username is used.
    def test_duplucate_username(self):
        response = self.client.post(
            self.register_url, self.user, format='text/html')

        response_dup = self.client.post(
            self.register_url, self.user_duplicate_username, format='text/html')
        self.assertEqual(response_dup.status_code, 400)

    # Checks if the user is not able to register with a short password.
    def test_cant_register_user_withshortpassword(self):
        response = self.client.post(
            self.register_url, self.user_short_password, format='text/html')
        self.assertEqual(response.status_code, 400)

    # Checks if the user is not able to register with unmatched passwords.
    def test_cant_register_user_with_unmatching_passwords(self):
        response = self.client.post(
            self.register_url, self.user_unmatching_password, format='text/html')
        self.assertEqual(response.status_code, 400)

    # Checks if the user is not able to register with an invalid email.
    def test_cant_register_user_with_invalid_email(self):
        response = self.client.post(
            self.register_url, self.user_invalid_email, format='text/html')
        self.assertEqual(response.status_code, 400)

    # Checks if the user is not able to register an invalid number.
    def test_cant_register_user_with_invalid_number(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(
            self.register_url, self.user_invalid_number, format='text/html')
        self.assertEqual(response.status_code, 400, msg="TEST FAILED: The user was able to register an invalid phone number")
    
    #Checks if the user is unable to register an invalid postal code.
    def test_cant_register_user_with_non_existing_postal_code(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(
            self.register_url, self.user_invalid_postal_code, format='text/html')
        self.assertEqual(response.status_code, 400, msg="TEST FAILED: The user was able to register an invalid postal code of 40222")

    
    

