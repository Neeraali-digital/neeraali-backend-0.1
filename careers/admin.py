from django.contrib import admin
from .models import Job, JobApplication

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

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ['get_applicant_name', 'job', 'application_type', 'status', 'created_at']
    list_filter = ['application_type', 'status', 'job__department', 'created_at']
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
