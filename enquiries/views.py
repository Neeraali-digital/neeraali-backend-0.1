from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Enquiry
from .serializers import EnquirySerializer, EnquiryCreateSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def create_enquiry(request):
    serializer = EnquiryCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Enquiry submitted successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Admin views
class AdminEnquiryListView(generics.ListAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_admin:
            return Enquiry.objects.none()
        return super().get_queryset()

class AdminEnquiryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if not self.request.user.is_admin:
            return Enquiry.objects.none()
        return super().get_queryset()
