from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from segmi.views import *
from django.http import HttpResponseRedirect, request


urlpatterns = [
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)