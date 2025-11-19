from django.urls import path
from . import views

urlpatterns = [
    # Public APIs
    path('', views.ServiceListView.as_view(), name='service-list'),
    path('<int:id>/', views.ServiceDetailView.as_view(), name='service-detail'),

    # Admin APIs
    path('admin/', views.AdminServiceListView.as_view(), name='admin-service-list'),
    path('admin/<int:id>/', views.AdminServiceDetailView.as_view(), name='admin-service-detail'),
    path('admin/update-order/', views.update_service_order, name='update-service-order'),
]
