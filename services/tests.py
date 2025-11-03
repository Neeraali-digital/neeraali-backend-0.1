from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Service

class ServiceTests(APITestCase):
    def setUp(self):
        self.service_data = {
            'name': 'Test Service',
            'description': 'Test Description',
            'features': ['Feature 1', 'Feature 2'],
            'price': '₹10,000',
            'status': 'active'
        }
        self.service = Service.objects.create(**self.service_data)
        self.list_url = reverse('service-list')
        self.detail_url = reverse('service-detail', kwargs={'id': self.service.pk})

    def test_get_services(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_get_service_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.service_data['name'])
