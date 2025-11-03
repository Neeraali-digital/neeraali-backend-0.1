from django.urls import path
from . import views

urlpatterns = [
    # Public APIs
    path('', views.BlogListView.as_view(), name='blog-list'),
    path('<int:id>/', views.BlogDetailView.as_view(), name='blog-detail'),

    # Admin APIs
    path('admin/', views.AdminBlogListView.as_view(), name='admin-blog-list'),
    path('admin/<int:id>/', views.AdminBlogDetailView.as_view(), name='admin-blog-detail'),
]
