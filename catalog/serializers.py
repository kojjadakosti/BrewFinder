from rest_framework import serializers

from catalog.models import Beer, BeerStyle, Brewery


class BeerStyleDetailSerializer(serializers.ModelSerializer):
    beers = serializers.StringRelatedField(many=True)

    class Meta:
        model = BeerStyle
        fields = '__all__'


class BeerStyleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerStyle
        fields = ['id', 'name']


class BreweryDetailSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    beers = serializers.StringRelatedField(many=True)

    class Meta:
        model = Brewery
        fields = '__all__'


class BreweryListSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Brewery
        fields = ['id', 'owner', 'name', 'location', 'email']


class BeerListSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()
    brewery = serializers.StringRelatedField()

    class Meta:
        model = Beer
        fields = ['id', 'name', 'abv', 'type', 'brewery']


class BeerDetailSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField()
    brewery = serializers.StringRelatedField()

    class Meta:
        model = Beer
        fields = '__all__'
