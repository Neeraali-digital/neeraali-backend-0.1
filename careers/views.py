from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Job, JobApplication
from .serializers import JobSerializer, JobListSerializer, JobApplicationSerializer

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

# Job Application Views
class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [AllowAny]
    
    def perform_create(self, serializer):
        application = serializer.save()
        # Update job applications count
        job = application.job
        job.applications = job.job_applications.count()
        job.save()

# Admin Job Application Views
class AdminJobApplicationListView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if not self.request.user.is_admin:
            return JobApplication.objects.none()
        job_id = self.request.query_params.get('job_id')
        if job_id:
            return JobApplication.objects.filter(job_id=job_id)
        return JobApplication.objects.all()

class AdminJobApplicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'
    
    def get_queryset(self):
        if not self.request.user.is_admin:
            return JobApplication.objects.none()
        return JobApplication.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        if not request.user.is_admin:
            return Response({'error': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        
        instance = self.get_object()
        job = instance.job
        instance.delete()
        job.applications = job.job_applications.count()
        job.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
