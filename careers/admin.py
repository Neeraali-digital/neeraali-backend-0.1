from django.contrib import admin
from .models import Job, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'type', 'status', 'created_at']
    list_filter = ['type', 'status']
    search_fields = ['title', 'company', 'location']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'company', 'location', 'type', 'experience', 'status')
        }),
        ('Job Details', {
            'fields': ('job_description', 'responsibilities', 'requirements', 'working_days_timings', 'how_to_apply')
        }),
        ('Metadata', {
            'fields': ('applications', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['get_applicant_name', 'job', 'application_type', 'status', 'created_at']
    list_filter = ['application_type', 'status', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'job__title']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Application Info', {
            'fields': ('job', 'application_type', 'status')
        }),
        ('Applicant Details', {
            'fields': ('first_name', 'last_name', 'email', 'phone')
        }),
        ('Referral Details', {
            'fields': ('friend_first_name', 'friend_last_name', 'friend_email', 'friend_phone'),
            'description': 'Only applicable for referral applications'
        }),
        ('Additional Information', {
            'fields': ('cover_letter', 'resume')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )
    
    def get_applicant_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_applicant_name.short_description = 'Applicant Name'
