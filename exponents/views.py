from authentication.permissions import IsModeratorOrOwnerOrReadOnly
from rest_framework import generics, viewsets

from exponents.models import (
    Exponent,
    Location,
    Partner,
    Review,
    ExponentCategory,
)
from exponents.serializers import (
    ExponentSerializer,
    LocationSerializer,
    PartnerSerializer,
    ReviewSerializer,
    ExponentCategorySerializer,
)


class ExponentViewSet(viewsets.ModelViewSet):
    serializer_class = ExponentSerializer
    queryset = Exponent.objects.all()
    permission_classes = [IsModeratorOrOwnerOrReadOnly]
    search_fields = ['user__username', 'user__emails']


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


class ExponentCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ExponentCategorySerializer
    queryset = ExponentCategory
    permission_classes = [IsModeratorOrOwnerOrReadOnly]
