from django.contrib import admin
from catalog.models import Beer, BeerStyle, Brewery

admin.site.register(Beer)
admin.site.register(BeerStyle)
admin.site.register(Brewery)