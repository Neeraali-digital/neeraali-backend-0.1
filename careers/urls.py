from django.urls import path
from . import views

urlpatterns = [
    # Public APIs
    path('', views.JobListView.as_view(), name='job-list'),
    path('<int:id>/', views.JobDetailView.as_view(), name='job-detail'),
    
    # Job Applications
    path('applications/', views.JobApplicationCreateView.as_view(), name='job-application-create'),

    # Admin APIs
    path('admin/', views.AdminJobListView.as_view(), name='admin-job-list'),
    path('admin/<int:id>/', views.AdminJobDetailView.as_view(), name='admin-job-detail'),
    
    # Admin Job Applications
    path('admin/applications/', views.AdminJobApplicationListView.as_view(), name='admin-job-application-list'),
    path('admin/applications/<int:pk>/', views.AdminJobApplicationDetailView.as_view(), name='admin-job-application-detail'),
    

]
