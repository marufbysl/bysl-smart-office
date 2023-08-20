from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Blog, BlogTag, BlogCategory
from .serializers import (
    BlogSerializer,BlogTagSerializer,BlogCategorySerializer
)

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogTagViewSet(viewsets.ModelViewSet):
    queryset = BlogTag.objects.all()
    serializer_class = BlogTagSerializer

class BlogCategoryViewSet(viewsets.ModelViewSet):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
