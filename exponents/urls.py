from django.urls import path
from rest_framework.routers import DefaultRouter

from exponents.views import (
    ExponentViewSet,
    LocationGetByExponentAPIView,
    LocationViewSet,
    PartnerGetByExponentApiView,
    PartnerViewSet,
    ReviewGetByExponentApiView,
    ReviewViewSet,
)

router = DefaultRouter()
router.register('locations', LocationViewSet, basename='location')
router.register('partners', PartnerViewSet, basename='partner')
router.register('reviews', ReviewViewSet, basename='review')
router.register('', ExponentViewSet, basename='exponent')

urlpatterns = [
    path('<int:pk>/locations/', LocationGetByExponentAPIView.as_view(), name='locations-get-by-exponent'),
    path('<int:pk>/partners/', PartnerGetByExponentApiView.as_view(), name='partners-get-by-exponent'),
    path('<int:pk>/reviews/', ReviewGetByExponentApiView.as_view(), name='reviews-get-by-exponent'),
    *router.urls,
]
