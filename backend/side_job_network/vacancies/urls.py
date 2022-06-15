from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacancies, name="vacancies"),
    path('<int:pk>', views.VacancyDetailView.as_view(), name='vacancy-detail')
]