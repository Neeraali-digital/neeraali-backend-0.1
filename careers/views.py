from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer, JobListSerializer

class JobListView(generics.ListAPIView):
    queryset = Job.objects.filter(status='active')
    serializer_class = JobListSerializer
    permission_classes = [AllowAny]

class JobDetailView(generics.RetrieveAPIView):
    queryset = Job.objects.filter(status='active')
    serializer_class = JobSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'

# Admin views
class AdminJobListView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_admin:
            return Job.objects.none()
        return super().get_queryset()

class AdminJobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if not self.request.user.is_admin:
            return Job.objects.none()
        return super().get_queryset()
