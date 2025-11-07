from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    category = serializers.CharField(source='related_to', read_only=True)
    readTime = serializers.SerializerMethodField()
    date = serializers.DateField(source='publish_date', format='%B %d, %Y', read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'excerpt', 'content', 'related_to', 'author', 'publish_date', 'read_time', 'status', 'image', 'category', 'date', 'readTime', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def get_readTime(self, obj):
        return f"{obj.read_time} min read"

class BlogListSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    category = serializers.CharField(source='related_to', read_only=True)
    readTime = serializers.SerializerMethodField()
    date = serializers.DateField(source='publish_date', format='%B %d, %Y', read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'excerpt', 'author', 'date', 'category', 'readTime', 'status', 'image_url']

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None

    def get_readTime(self, obj):
        return f"{obj.read_time} min read"
