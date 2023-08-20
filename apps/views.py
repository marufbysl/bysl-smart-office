from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import App, AppFeature, Pricing, PlanFeature, PricingPlanFeature
from .serializers import (
    AppSerializer, AppFeatureSerializer,
    PricingSerializer, PlanFeatureSerializer,
    PricingPlanFeatureSerializer,
)

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

class AppFeatureViewSet(viewsets.ModelViewSet):
    queryset = AppFeature.objects.all()
    serializer_class = AppFeatureSerializer

class PricingViewSet(viewsets.ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

class PlanFeatureViewSet(viewsets.ModelViewSet):
    queryset = PlanFeature.objects.all()
    serializer_class = PlanFeatureSerializer

class PricingPlanFeatureViewSet(viewsets.ModelViewSet):
    queryset = PricingPlanFeature.objects.all()
    serializer_class = PricingPlanFeatureSerializer
