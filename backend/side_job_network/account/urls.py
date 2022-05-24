from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
]