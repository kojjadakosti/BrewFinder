from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_customer = models.BooleanField(default=True)
    is_brewery_owner = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='users_images', null=True, blank=True)

    def __str__(self):
        return self.username
