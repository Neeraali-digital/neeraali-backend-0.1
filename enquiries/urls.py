from django.urls import path
from . import views

urlpatterns = [
    # Public APIs
    path('', views.create_enquiry, name='create-enquiry'),

    # Admin APIs
    path('admin/', views.AdminEnquiryListView.as_view(), name='admin-enquiry-list'),
    path('admin/<int:id>/', views.AdminEnquiryDetailView.as_view(), name='admin-enquiry-detail'),
]
