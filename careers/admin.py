from django.contrib import admin
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'department', 'location', 'type', 'status', 'is_featured', 'created_at']
    list_filter = ['type', 'status', 'is_featured', 'remote_work_available', 'department']
    search_fields = ['title', 'department', 'location']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'department', 'location', 'type', 'experience', 'status')
        }),
        ('Job Details', {
            'fields': ('description', 'requirements', 'salary_range')
        }),
        ('Contact Information', {
            'fields': ('contact_email',),
            'description': 'Contact email will default to hr@neeraali.com if not provided'
        }),
        ('Additional Settings', {
            'fields': ('shift_work', 'career_area', 'contractual_location', 'term_of_employment', 
                      'application_deadline', 'is_featured', 'remote_work_available')
        }),
        ('Detailed Descriptions', {
            'fields': ('job_description', 'the_opportunity', 'what_youll_be_doing', 
                      'your_work_location', 'who_you_are', 'security_vetting', 
                      'pay', 'benefits_and_culture', 'additional_information'),
            'classes': ('collapse',)
        }),
        ('Metadata', {
            'fields': ('applications', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
