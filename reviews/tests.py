from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Review

class ReviewTests(APITestCase):
    def setUp(self):
        self.review_data = {
            'name': 'Test User',
            'company': 'Test Company',
            'rating': 5,
            'review': 'Test Review'
        }
        self.list_url = reverse('review-list')
        self.create_url = reverse('create-review')

    def test_get_reviews(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_review(self):
        response = self.client.post(self.create_url, self.review_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', response.data)
