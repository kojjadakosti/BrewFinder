from rest_framework import viewsets
from catalog.models import Beer, BeerStyle, Brewery
from catalog.serializers import BeerSerializer, BeerStyleSerializer, BrewerySerializer


class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer


class BeerStyleViewSet(viewsets.ModelViewSet):
    queryset = BeerStyle.objects.all()
    serializer_class = BeerStyleSerializer


class BreweryViewSet(viewsets.ModelViewSet):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer
