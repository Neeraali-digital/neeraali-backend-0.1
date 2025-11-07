from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from services.models import Service
from blogs.models import Blog
from enquiries.models import Enquiry
from reviews.models import Review
from careers.models import Job

@swagger_auto_schema(method='get')
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_stats(request):
    if not request.user.is_admin:
        return Response({"error": "Unauthorized"}, status=403)

    stats = {
        "totalBlogs": Blog.objects.count(),
        "totalServices": Service.objects.count(),
        "totalEnquiries": Enquiry.objects.count(),
        "totalReviews": Review.objects.count(),
        "totalCareers": Job.objects.count(),
        "activeJobs": Job.objects.filter(status='active').count(),
        "publishedBlogs": Blog.objects.filter(status='published').count(),
        "activeServices": Service.objects.filter(status='active').count(),
        "newEnquiries": Enquiry.objects.filter(status='new').count(),
        "pendingReviews": Review.objects.filter(status='pending').count(),
    }

    return Response(stats)
