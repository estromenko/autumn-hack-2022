from rest_framework import viewsets

from exponents.models import Exponent
from exponents.serializers import ExponentSerializer


class ExponentViewSet(viewsets.ModelViewSet):
    serializer_class = ExponentSerializer
    queryset = Exponent.objects.all()
