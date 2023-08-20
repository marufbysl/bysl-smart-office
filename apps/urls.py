from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AppViewSet, AppFeatureViewSet,
    PricingViewSet, PlanFeatureViewSet,
    PricingPlanFeatureViewSet,
)

router = DefaultRouter()
router.register(r'apps', AppViewSet)
router.register(r'app-features', AppFeatureViewSet)
router.register(r'pricings', PricingViewSet)
router.register(r'plan-features', PlanFeatureViewSet)
router.register(r'pricing-plan-features', PricingPlanFeatureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
