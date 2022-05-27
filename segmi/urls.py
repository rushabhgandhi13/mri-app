from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from segmi.views import *
from django.http import HttpResponseRedirect, request


urlpatterns = [
    path('', views.home, name='home'),
    path('doctor/<int:id>', views.doctor, name='doctor'),
    path('appointment/<int:id>', views.appointment, name='appointment'),
    path('report/<int:id>', views.patientReport, name='report'),
    path('aplist/', views.aplist, name='aplist'),
    path('lab/', views.lab, name='lab'),
    path('labreports/', views.labreports, name='labreports'),
    path('myreport/', views.myreport, name='myreport'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)