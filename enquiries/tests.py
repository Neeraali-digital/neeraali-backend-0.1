from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Enquiry

class EnquiryTests(APITestCase):
    def setUp(self):
        self.enquiry_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'phone': '1234567890',
            'service': 'Test Service',
            'message': 'Test Message'
        }
        self.create_url = reverse('create-enquiry')

    def test_create_enquiry(self):
        response = self.client.post(self.create_url, self.enquiry_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', response.data)
