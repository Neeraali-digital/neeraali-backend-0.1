from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Service
from .serializers import ServiceSerializer, ServiceListSerializer

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.filter(status='active')
    serializer_class = ServiceListSerializer
    permission_classes = [AllowAny]

class ServiceDetailView(generics.RetrieveAPIView):
    queryset = Service.objects.filter(status='active')
    serializer_class = ServiceSerializer
    permission_classes = [AllowAny]
    lookup_field = 'id'

# Admin views
class AdminServiceListView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_admin:
            return Service.objects.none()
        return super().get_queryset()

class AdminServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        if not self.request.user.is_admin:
            return Service.objects.none()
        return super().get_queryset()

    def update(self, request, *args, **kwargs):
        partial = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_service_order(request):
    if not request.user.is_admin:
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)
    
    service_orders = request.data.get('service_orders', [])
    
    # Use transaction to ensure atomicity
    from django.db import transaction
    
    try:
        with transaction.atomic():
            for item in service_orders:
                service_id = item.get('id')
                new_order = item.get('order')
                
                service = Service.objects.get(id=service_id)
                service.order = new_order
                service.save(update_fields=['order'])
                
    except Service.DoesNotExist:
        return Response({'error': 'Service not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'message': 'Service order updated successfully'}, status=status.HTTP_200_OK)
