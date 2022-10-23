from django.urls import path
from rest_framework.routers import DefaultRouter

from exponents.views import (
    ExponentViewSet,
    LocationGetByExponentAPIView,
    LocationViewSet,
    PartnerGetByExponentApiView,
    PartnerViewSet,
    ProductGetByExponentApiView,
    ProductViewSet,
    ProductCategoryViewSet,
    ProductGetByCategoryApiView,
    ReviewGetByExponentApiView,
    ReviewViewSet,
    ExponentGetByCategoryAPIView,
    ExponentCategoryViewSet,
)

router = DefaultRouter()
router.register('locations', LocationViewSet, basename='location')
router.register('partners', PartnerViewSet, basename='partner')
router.register('products', ProductViewSet, basename='product')
router.register('products-categories', ProductCategoryViewSet, basename='product_categories')
router.register('reviews', ReviewViewSet, basename='review')
router.register('exponents-categories', ExponentCategoryViewSet, basename='exponents_category')
router.register('exponents', ExponentViewSet, basename='exponent')

urlpatterns = [
    path('exponents/<int:pk>/locations/', LocationGetByExponentAPIView.as_view(),
         name='locations-get-by-exponent'),
    path('exponents/<int:pk>/partners/', PartnerGetByExponentApiView.as_view(),
         name='partners-get-by-exponent'),
    path('exponents/<int:pk>/products/', ProductGetByExponentApiView.as_view(),
         name='partners-get-by-exponent'),
    path('products-categories/<int:pk>/products/', ProductGetByCategoryApiView.as_view(),
         name='products-categories-get-by-exponent'),
    path('exponents-categories/<int:pk>/exponents/', ExponentGetByCategoryAPIView.as_view(),
         name='exponents-categories-get-by-exponent'),
    path('exponents/<int:pk>/reviews/', ReviewGetByExponentApiView.as_view(),
         name='reviews-get-by-exponent'),
    *router.urls,
]
