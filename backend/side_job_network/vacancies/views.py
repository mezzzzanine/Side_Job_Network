from django.shortcuts import render
from django.http import HttpResponse


def vacancies(request):
    return render(request, "vacancies/vacancies.html")
