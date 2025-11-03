from django.urls import path
from . import views

urlpatterns = [
    # Public APIs
    path('', views.JobListView.as_view(), name='job-list'),
    path('<int:id>/', views.JobDetailView.as_view(), name='job-detail'),

    # Admin APIs
    path('admin/', views.AdminJobListView.as_view(), name='admin-job-list'),
    path('admin/<int:id>/', views.AdminJobDetailView.as_view(), name='admin-job-detail'),
]
