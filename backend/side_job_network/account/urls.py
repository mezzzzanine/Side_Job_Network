from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
    path('sign-in', views.signin, name='sign_in'),
    path('sign-up', views.signup, name='sign_in'),
    path('profile', views.profile, name='profile'),
    path('my-profile', views.myprofile, name='profile'),
]