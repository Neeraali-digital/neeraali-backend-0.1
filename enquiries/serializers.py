from rest_framework import serializers
from .models import Enquiry

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'

class EnquiryCreateSerializer(serializers.ModelSerializer):
    enquiry_type = serializers.ChoiceField(choices=Enquiry.ENQUIRY_TYPE_CHOICES, default='general')

    class Meta:
        model = Enquiry
        fields = ['enquiry_type', 'name', 'email', 'phone', 'company', 'service', 'message']
