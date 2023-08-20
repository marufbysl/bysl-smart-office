from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BlogViewSet,BlogTagViewSet,BlogCategoryViewSet
)

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'blog-tags', BlogTagViewSet)
router.register(r'blog-categories', BlogCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
