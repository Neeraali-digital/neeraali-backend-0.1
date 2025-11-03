from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None

class BlogListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'excerpt', 'author', 'publish_date', 'status', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None
