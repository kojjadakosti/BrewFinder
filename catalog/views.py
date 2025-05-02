from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from catalog.models import Beer, BeerStyle, Brewery
from catalog.permissions import IsAdminUserOrReadOnly, IsBreweryOwnerOrAdmin
from catalog.serializers import (
    BeerListSerializer, BeerDetailSerializer,
    BeerStyleListSerializer, BeerStyleDetailSerializer,
    BreweryListSerializer, BreweryDetailSerializer
)


class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    permission_classes = [IsBreweryOwnerOrAdmin]

    def get_serializer_class(self):
        return BeerListSerializer if self.action == 'list' else BeerDetailSerializer

    def perform_create(self, serializer):
        brewery = serializer.validated_data.get('brewery')
        if not self.request.user.is_superuser and brewery.owner != self.request.user:
            raise PermissionDenied("Вы не являетесь владельцем этой пивоварни.")
        serializer.save()


class BeerStyleViewSet(viewsets.ModelViewSet):
    queryset = BeerStyle.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]

    def get_serializer_class(self):
        return BeerStyleListSerializer if self.action == 'list' else BeerStyleDetailSerializer


class BreweryViewSet(viewsets.ModelViewSet):
    queryset = Brewery.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]

    def get_serializer_class(self):
        return BreweryListSerializer if self.action == 'list' else BreweryDetailSerializer
