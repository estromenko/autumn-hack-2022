from rest_framework.routers import DefaultRouter
from exponents.views import ExponentViewSet


router = DefaultRouter()
router.register('', ExponentViewSet, basename='exponent')

urlpatterns = [
    *router.urls,
]
