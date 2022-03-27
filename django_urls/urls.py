from django.urls import path, include
from django_urls.views import index, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/', include('django.contrib.auth.urls'))
]
