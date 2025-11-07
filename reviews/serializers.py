from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Review
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Review
        fields = ['id', 'name', 'company', 'rating', 'review', 'image', 'date']

class ReviewCreateSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Review
        fields = ['name', 'company', 'rating', 'review', 'image']
