from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Review
from .serializers import ReviewSerializer, ReviewListSerializer, ReviewCreateSerializer

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.filter(status='approved')
    serializer_class = ReviewListSerializer
    permission_classes = [AllowAny]

@swagger_auto_schema(method='post', request_body=ReviewCreateSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def create_review(request):
    serializer = ReviewCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Review submitted successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin views
class AdminReviewListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_admin:
            return Review.objects.none()
        return super().get_queryset()

class AdminReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if not self.request.user.is_admin:
            return Review.objects.none()
        return super().get_queryset()
