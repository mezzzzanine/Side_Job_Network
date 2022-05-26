from distutils.log import error
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vacancy
from .forms import VacancyForm

def profile(request):
    vacancies = Vacancy.objects.all()
    return render(request, "account/profile.html", { 'vacancies':vacancies })


def settings(request):
    return render(request, "account/settings.html")


def signin(request):
    return render(request, "account/sign_in.html")


def signup(request):
    return render(request, "account/sign_up.html")


def create(request):
    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/my-profile')
    form = VacancyForm
    data={
        'form': form
        }
    return render(request, "account/create.html", data)


def myprofile(request):
    vacancies = Vacancy.objects.all()
    return render(request, "account/my_profile.html", { 'vacancies':vacancies })