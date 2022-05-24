from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('support', views.support, name='support'),
    path('sponsorship', views.sponsorship, name='sponsorship'),
    path('privacy-policy', views.privacy_policy, name='privacy-policy'),
]