from authentication.permissions import IsModeratorOrOwnerOrReadOnly
from rest_framework import generics, viewsets

from exponents.models import (
    Exponent,
    Location,
    Partner,
    Product,
    ProductCategory,
    Review,
    ExponentCategory,
)
from exponents.serializers import (
    ExponentSerializer,
    LocationSerializer,
    PartnerSerializer,
    ProductSerializer,
    ProductCategorySerializer,
    ReviewSerializer,
    ExponentCategorySerializer,
)


class ExponentViewSet(viewsets.ModelViewSet):
    serializer_class = ExponentSerializer
    queryset = Exponent.objects.all()
    permission_classes = [IsModeratorOrOwnerOrReadOnly]
    search_fields = ['user__username', 'user__emails']


class ExponentCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ExponentCategorySerializer
    queryset = ExponentCategory.objects.all()
    permission_classes = [IsModeratorOrOwnerOrReadOnly]


class ExponentGetByCategoryAPIView(generics.ListAPIView):
    serializer_class = ExponentSerializer
    permission_classes = [IsModeratorOrOwnerOrReadOnly]

    def get_queryset(self):
        category_id = self.kwargs['pk']
        category_exponents = Exponent.objects.filter(category=category_id)

        return category_exponents


class LocationGetByExponentAPIView(generics.ListAPIView):
    serializer_class = LocationSerializer
    permission_classes = [IsModeratorOrOwnerOrReadOnly]

    def get_queryset(self):
        exponent_id = self.kwargs['pk']
        exponent_locations = Location.objects.filter(exponent=exponent_id)

        return exponent_locations


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    permission_classes = [IsModeratorOrOwnerOrReadOnly]


class PartnerViewSet(viewsets.ModelViewSet):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.all()
    permission_classes = [IsModeratorOrOwnerOrReadOnly]


class PartnerGetByExponentApiView(generics.ListAPIView):
    serializer_class = PartnerSerializer
    permission_classes = [IsModeratorOrOwnerOrReadOnly]

    def get_queryset(self):
        exponent_id = self.kwargs['pk']
        exponent_reviews = Partner.objects.filter(exponent=exponent_id)

        return exponent_reviews


class ProductGetByCategoryApiView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsModeratorOrOwnerOrReadOnly]

    def get_queryset(self):
        category = self.kwargs['pk']
        category_products = Product.objects.filter(category=category)

        return category_products


class ProductCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.all()
    permission_classes = [IsModeratorOrOwnerOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductCategorySerializer
    queryset = Product.objects.all()
    permission_classes = [IsModeratorOrOwnerOrReadOnly]


class ProductGetByExponentApiView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsModeratorOrOwnerOrReadOnly]

    def get_queryset(self):
        exponent_id = self.kwargs['pk']
        exponent_products = Product.objects.filter(exponent=exponent_id)

        return exponent_products


class ReviewGetByExponentApiView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsModeratorOrOwnerOrReadOnly]

    def get_queryset(self):
        exponent_id = self.kwargs['pk']
        exponent_reviews = Review.objects.filter(exponent=exponent_id)

        return exponent_reviews


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
    permission_classes = [IsModeratorOrOwnerOrReadOnly]
