from django.urls import path
from django_urls.views import index

urlpatterns = [
    path('', index, name='index')
]
