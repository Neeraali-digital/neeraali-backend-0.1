from django.urls import path
from . import views

urlpatterns = [
    # Public APIs
    path('', views.ReviewListView.as_view(), name='review-list'),
    path('submit/', views.create_review, name='create-review'),

    # Admin APIs
    path('admin/', views.AdminReviewListView.as_view(), name='admin-review-list'),
    path('admin/<int:id>/', views.AdminReviewDetailView.as_view(), name='admin-review-detail'),
]
