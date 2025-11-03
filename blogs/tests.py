from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Blog

class BlogTests(APITestCase):
    def setUp(self):
        self.blog_data = {
            'title': 'Test Blog',
            'excerpt': 'Test Excerpt',
            'author': 'Test Author',
            'publish_date': '2024-01-01',
            'status': 'published',
            'content': 'Test Content'
        }
        self.blog = Blog.objects.create(**self.blog_data)
        self.list_url = reverse('blog-list')
        self.detail_url = reverse('blog-detail', kwargs={'id': self.blog.pk})

    def test_get_blogs(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_get_blog_detail(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.blog_data['title'])
