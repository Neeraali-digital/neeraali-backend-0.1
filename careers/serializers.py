from rest_framework import serializers
from .models import Job, JobApplication

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class JobListSerializer(serializers.ModelSerializer):
    applications_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Job
        fields = [
            'id', 'title', 'department', 'location', 'type', 'experience', 'status', 'applications',
            'shift_work', 'career_area', 'contractual_location', 'term_of_employment', 'applications_count'
        ]
    
    def get_applications_count(self, obj):
        return obj.job_applications.count()

class JobApplicationSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)
    
    class Meta:
        model = JobApplication
        fields = '__all__'
        
    def validate(self, data):
        # Validate referral fields if application type is referral
        if data.get('application_type') == 'referral':
            required_fields = ['friend_first_name', 'friend_last_name', 'friend_email', 'friend_phone']
            for field in required_fields:
                if not data.get(field):
                    raise serializers.ValidationError(f"{field.replace('_', ' ').title()} is required for referrals")
        return data

class JobApplicationListSerializer(serializers.ModelSerializer):
    job_title = serializers.CharField(source='job.title', read_only=True)
    applicant_name = serializers.SerializerMethodField()
    
    class Meta:
        model = JobApplication
        fields = ['id', 'job_title', 'applicant_name', 'application_type', 'status', 'created_at']
    
    def get_applicant_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
