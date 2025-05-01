from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('catalog/', include('catalog.urls')),
]