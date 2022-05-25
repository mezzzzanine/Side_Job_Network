from django.shortcuts import render
from django.http import HttpResponse
from .models import Vacancy


def profile(request):
    vacancies = Vacancy.objects.all()
    return render(request, "account/profile.html", { "vacancies":vacancies })


def settings(request):
    return render(request, "account/settings.html")


def signin(request):
    return render(request, "account/sign_in.html")


def signup(request):
    return render(request, "account/sign_up.html")


def myprofile(request):
    return render(request, "account/my_profile.html")