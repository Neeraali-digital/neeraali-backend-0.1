from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class DashboardTests(APITestCase):
    def setUp(self):
        self.stats_url = reverse('dashboard-stats')

    def test_get_dashboard_stats(self):
        response = self.client.get(self.stats_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_blogs', response.data)
        self.assertIn('total_services', response.data)
        self.assertIn('total_enquiries', response.data)
        self.assertIn('total_reviews', response.data)
        self.assertIn('total_jobs', response.data)
