from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Job

class JobTests(APITestCase):
    def setUp(self):
        self.job_data = {
            'title': 'Test Job',
            'department': 'Test Department',
            'location': 'Test Location',
            'type': 'full-time',
            'experience': '2-3 years',
            'description': 'Test Description',
            'requirements': ['Req 1', 'Req 2'],
            'status': 'active'
        }
        self.job = Job.objects.create(**self.job_data)
        self.list_url = reverse('job-list')
        self.detail_url = reverse('job-detail', kwargs={'id': self.job.pk})

    def test_get_jobs(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_get_job_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.job_data['title'])
