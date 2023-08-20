from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FqaSerializerViewSet,CustomerSerializerViewSet,CustomerReviewSerializerViewSet,ContactMessageSerializerViewSet,SubscriptionSerializerViewSet
)

router = DefaultRouter()
router.register(r'fqa', FqaSerializerViewSet)
router.register(r'customers', CustomerSerializerViewSet)
router.register(r'customer-reviews', CustomerReviewSerializerViewSet)
router.register(r'contact-messages', ContactMessageSerializerViewSet)
router.register(r'subscriptions', SubscriptionSerializerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
