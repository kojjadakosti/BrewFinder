from django.urls import include, path
from rest_framework.routers import DefaultRouter

from catalog.views import BeerStyleViewSet, BeerViewSet, BreweryViewSet

app_name = 'catalog'

router = DefaultRouter()
router.register(r'beers', BeerViewSet)
router.register(r'beer-styles', BeerStyleViewSet)
router.register(r'breweries', BreweryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
