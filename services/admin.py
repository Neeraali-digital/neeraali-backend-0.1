from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'price', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['status']
    ordering = ['-created_at']
