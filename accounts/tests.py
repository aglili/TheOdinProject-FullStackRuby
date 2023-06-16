from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import CustomUser
# Create your tests here.
class UserSignUpLoginTests(APITestCase):
    def test_signup(self):
        url = reverse('sign_up')
        data = {
            'first_name': 'Elikem',
            'last_name': 'Doe',
            'username': 'elidoe',
            'email': 'elikemdoe@example.com',
            'password': 'password123'
        }

        response = self.client.post(url,data,format='json')

        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(),1)
        self.assertEqual(CustomUser.objects.get().username,"elidoe")


        
    def test_login(self):
        url = reverse('login')  # Replace 'login' with the actual URL name for your login endpoint
        user = CustomUser.objects.create_user(username='johndoe', password='password123')
        data = {
            'username': 'johndoe',
            'password': 'password123'
        }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Login successful')