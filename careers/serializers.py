from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'id', 'title', 'department', 'location', 'type', 'experience', 'status', 'applications',
            'shift_work', 'career_area', 'contractual_location', 'term_of_employment'
        ]
