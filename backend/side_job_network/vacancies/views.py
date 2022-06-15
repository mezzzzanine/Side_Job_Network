from turtle import title
from django.shortcuts import render
from account.models import Vacancy
from django.views.generic import DetailView
from django.core.paginator import Paginator

def vacancies(request):
    search_query = request.GET.get('search','')
    if search_query:
        vacancies = Vacancy.objects.filter(title__icontains=search_query, country__icontains=search_query)
    else:
        vacancies = Vacancy.objects.all()

    # Set up paginators
    paginator = Paginator(Vacancy.objects.all(), 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "vacancies/vacancies.html", {'page_obj':page_obj, 'vacancies':vacancies})

class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy.html'
    context_object_name = 'vacancy'