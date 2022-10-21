from rest_framework import serializers

from exponents.models import Exponent


class ExponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exponent
        fields = serializers.ALL_FIELDS
