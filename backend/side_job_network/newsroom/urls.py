from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.newsroom, name='newsroom'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='newsroom-detail')
]