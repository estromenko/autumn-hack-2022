from rest_framework import viewsets
from authentication.permissions import IsModeratorOrOwnerOrReadOnly

from exponents.models import Exponent
from exponents.serializers import ExponentSerializer


class ExponentViewSet(viewsets.ModelViewSet):
    serializer_class = ExponentSerializer
    queryset = Exponent.objects.all()
    permission_classes = [IsModeratorOrOwnerOrReadOnly]
