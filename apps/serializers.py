from rest_framework import serializers
from .models import App, AppFeature, Pricing, PlanFeature, PricingPlanFeature

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

class AppFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppFeature
        fields = '__all__'

class PricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricing
        fields = '__all__'

class PlanFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanFeature
        fields = '__all__'

class PricingPlanFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlanFeature
        fields = '__all__'
