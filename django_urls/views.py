from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def index(request):
    return HttpResponse('Hello, World!')


class IndexView(TemplateView):
    template_name = 'django_urls/index.html'
