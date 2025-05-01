from rest_framework import serializers

from catalog.models import BeerStyle, Brewery, Beer


class BeerStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerStyle
        fields = '__all__'


class BrewerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Brewery
        fields = '__all__'


class BeerSerializer(serializers.ModelSerializer):
    type = BeerStyleSerializer()
    brewery = BrewerySerializer()

    class Meta:
        model = Beer
        fields = '__all__'
