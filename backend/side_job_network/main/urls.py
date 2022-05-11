from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about-us', views.about),
    path('support', views.support),
    path('sponsorship', views.sponsorship),
    path('privacy-policy', views.privacy_policy),
]