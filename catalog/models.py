from django.db import models

from accounts.models import User


class Brewery(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    location = models.CharField(max_length=64)
    owner = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class BeerStyle(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Beer(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1024)
    abv = models.DecimalField(max_digits=4, decimal_places=2)
    type = models.ForeignKey(to=BeerStyle, on_delete=models.SET_NULL, null=True, related_name='beers')
    brewery = models.ForeignKey(to=Brewery, on_delete=models.CASCADE, related_name='beers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
