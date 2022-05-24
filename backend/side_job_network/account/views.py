from django.shortcuts import render
from django.http import HttpResponse


def profile(request):
    return render(request, "account/profile.html")


def settings(request):
    return render(request, "account/settings.html")


def signin(request):
    return render(request, "account/sign_in.html")


def signup(request):
    return render(request, "account/sign_up.html")

