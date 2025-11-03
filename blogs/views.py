from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer, BlogListSerializer

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.filter(status='published')
    serializer_class = BlogListSerializer
    permission_classes = [AllowAny]

class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.filter(status='published')
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'

# Admin views
class AdminBlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_admin:
            return Blog.objects.none()
        return super().get_queryset()

class AdminBlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if not self.request.user.is_admin:
            return Blog.objects.none()
        return super().get_queryset()
