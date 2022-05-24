from django.shortcuts import render
from django.http import HttpResponse


def profile(request):
    return render(request, "account/profile.html")


def settings(request):
    return render(request, "account/settings.html")


