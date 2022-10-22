from rest_framework import serializers

from exponents.models import (
    Exponent,
    Location,
    Partner,
    Review,
    ExponentCategory,
)


class ExponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exponent
        fields = serializers.ALL_FIELDS


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = serializers.ALL_FIELDS


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = serializers.ALL_FIELDS


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = serializers.ALL_FIELDS


class ExponentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExponentCategory
        fields = serializers.ALL_FIELDS
