from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from .models import Fqa, Customer, CustomerReview,ContactMessage,Subscription
from .serializers import (
    FqaSerializer,CustomerSerializer,CustomerReviewSerializer,ContactMessageSerializer,SubscriptionSerializer
)

class FqaSerializerViewSet(viewsets.ModelViewSet):
    queryset = Fqa.objects.all()
    serializer_class = FqaSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CustomerSerializerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerReviewSerializerViewSet(viewsets.ModelViewSet):
    queryset = CustomerReview.objects.all()
    serializer_class = CustomerReviewSerializer

class ContactMessageSerializerViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

class SubscriptionSerializerViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
