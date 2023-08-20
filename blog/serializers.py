from rest_framework import serializers
from .models import Blog,BlogTag,BlogCategory

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogTag
        fields = '__all__'

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = '__all__'
