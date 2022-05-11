from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "main/index.html")

def about(request):
    return render(request, "main/about.html")

def support(request):
    return render(request, "main/support.html")

def sponsorship(request):
    return render(request, "main/sponsorship.html")

def privacy_policy(request):
    return render(request, "main/privacy_policy.html")




