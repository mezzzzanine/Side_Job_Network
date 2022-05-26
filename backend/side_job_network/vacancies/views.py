from django.shortcuts import render
from account.models import Vacancy
from django.views.generic import DetailView

def vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, "vacancies/vacancies.html", {'vacancies':vacancies})

class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy.html'
    context_object_name = 'vacancy'