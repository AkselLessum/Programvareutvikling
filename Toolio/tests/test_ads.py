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
        # creates a User object with the specified credentials
        CustomUser.objects.create_user(**self.credentials)
        bruker = CustomUser.objects.get(username="brukernavn")
        
        self.ad_data = { #annonse
            "user": bruker,
            "isRequest": False,
            "isRented": False,
            "title": "Test Ad",
            "category": "Snekring og tømrearbeid",
            "date": "2023-03-15",
            "price": 100,
            "description": "Test Description",
            "image": SimpleUploadedFile("test_image.png", b"file_content", content_type="image/png")
        }

        self.ad_data_request = { #ønskes leid annonse
            "user": bruker,
            "isRequest": True,
            "title": "Test Request Ad",
            "category": "Snekring og tømrearbeid",
            "date": "2023-03-15",
            "price": 100,
            "description": "Test Description"
        }

        self.invalid_ad_data = {
            "user": bruker,
            "isRequest": False,
            "isRented": False,
            "title": "",  # title is required
            "category": "Snekring og tømrearbeid",
            "date": "2023-03-15",
            "price": 100,
            "description": "Test Description",
            "image": SimpleUploadedFile("test_image.png", b"file_content", content_type="image/png")
        }
        self.ad = ad.objects.create(**self.ad_data)
        self.ad_request = ad.objects.create(**self.ad_data_request)

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

    def test_edit_ad(self): #tests if an "annonse" can be edited
        # Creates a new ad (annonse) object

        self.client.login(username="brukernavn", password="Bananmann1")
        response = self.client.post(reverse('createAd'), data=self.ad_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ad.objects.filter(title="Test Ad").exists(), msg="FAILED: ad was not created")

        # Get the newly created ad object and its id
        ad_obj = ad.objects.get(title="Test Ad")
        ad_id = ad_obj.id

        # Create a new data dictionary with the updated ad information
        updated_data = {
        "title": "Updated Title",
        "category": "Hagearbeid",
        "date": "2023-03-16",
        "price": 200,
        "description": "Updated Description",
        "image": SimpleUploadedFile("test_image.png", b"file_content", content_type="image/png"),
        "isRented": True
        }

        # Simulate a form submission to update the ad object
        self.edit_url = reverse('edit_ad', args=[ad_id])
        response = self.client.post(self.edit_url, data=updated_data, follow=True)
        self.assertEqual(response.status_code, 200)
        # Get the updated ad object and check if the values are updated correctly
        ad_obj = ad.objects.get(id=ad_id)
        print()
        print("Asserting title change... Title should now be Updated Title:   ", ad_obj.title)
        self.assertEqual(ad_obj.title, "Updated Title", msg="FAILED TEST: ad title was not updated")
        print()
        print("Asserting category change... Category should now be Hagearbeid:   ", ad_obj.category)
        self.assertEqual(ad_obj.category, "Hagearbeid", msg="FAILED TEST: ad category was not updated")
        print()
        print("Asserting date change... Date should now be = 2023-03-16:   ", ad_obj.date)
        self.assertEqual(str(ad_obj.date), "2023-03-16", msg="FAILED TEST: ad date was not updated")
        print()
        print("Asserting price change...   Price should now be 200:   ", ad_obj.price)
        self.assertEqual(ad_obj.price, 200, msg="FAILED TEST: ad price was not updated")
        print()
        print("Asserting description change...   Description should now be Updated Description:   ",ad_obj.description)
        self.assertEqual(ad_obj.description, "Updated Description", msg="FAILED TEST: ad description was not updated")
        print()
        print("Asserting isRented boolean value...   isRented should now be True:   ", ad_obj.isRented)
        self.assertEqual(ad_obj.isRented, True, msg="FAILED TEST: isRented boolean value was not updated")
        print()
    
    def test_edit_request_ad(self): #tests if an "ønskes leid" can be edited, as this uses a different form
        # Creates a new request ad object

        self.client.login(username="brukernavn", password="Bananmann1")
        response = self.client.post(reverse('createAd'), data=self.ad_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ad.objects.filter(title="Test Request Ad").exists(), msg="FAILED: ad was not created")

        # Get the newly created ad object and its id
        ad_obj = ad.objects.get(title="Test Request Ad")
        ad_id = ad_obj.id

        

        # Creates a new data dictionary with the updated ad information
        updated_data = {
        "title": "Updated Request Title",
        "category": "Hagearbeid",
        "date": "2023-03-16",
        "price": 200,
        "description": "Updated Request Description",
        }

        # Simulate a form submission to update the ad object
        self.edit_url = reverse('edit_ad', args=[ad_id])
        response = self.client.post(self.edit_url, data=updated_data, follow=True)
        self.assertEqual(response.status_code, 200)
        # Get the updated ad object and check if the values are updated correctly
        ad_obj = ad.objects.get(id=ad_id)
        print()
        print("Asserting request title change... Title should now be Updated Request Title:   ", ad_obj.title)
        self.assertEqual(ad_obj.title, "Updated Request Title", msg="FAILED TEST: ad title was not updated")
        print()
        print("Asserting request category change... Category should now be Hagearbeid:   ", ad_obj.category)
        self.assertEqual(ad_obj.category, "Hagearbeid", msg="FAILED TEST: ad category was not updated")
        print()
        print("Asserting request date change... Date should now be = 2023-03-16:   ", ad_obj.date)
        self.assertEqual(str(ad_obj.date), "2023-03-16", msg="FAILED TEST: ad date was not updated")
        print()
        print("Asserting request price change...   Price should now be 200:   ", ad_obj.price)
        self.assertEqual(ad_obj.price, 200, msg="FAILED TEST: ad price was not updated")
        print()
        print("Asserting request description change...   Description should now be Updated Request Description:   ",ad_obj.description)
        self.assertEqual(ad_obj.description, "Updated Request Description", msg="FAILED TEST: ad description was not updated")
        print()

    #Tests if an ad is succesfully deleted from the database
    def test_delete_ad(self): 
        # Login as the user who created the ad
        self.client.login(username="brukernavn", password="Bananmann1")
    
        # Creates a new ad object
        response = self.client.post(self.ad_url, data=self.ad_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ad.objects.filter(title="Test Ad").exists(), msg="FAILED: ad was not created")
    
        # Gets the ad object and its id
        ad_obj = ad.objects.get(title="Test Ad")
        ad_id = ad_obj.id
    
        # Simulate a form submission to delete the ad object
        self.delete_url = reverse('delete_ad', args=[ad_id])
        response = self.client.post(self.delete_url, follow=True)
        self.assertEqual(response.status_code, 200)
    
        # Check that the ad object no longer exists in the database
        print()
        print("Asserting ad deletion...   ")
        self.assertFalse(ad.objects.filter(title="Test Ad").exists(), msg="FAILED: ad was not deleted")
        print("Ad deletion asserted")
        print()




    


    
