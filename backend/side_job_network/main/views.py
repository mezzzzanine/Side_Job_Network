from logging import exception
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import Http404

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

def pageNotFound(request, exception):
    return render(request, "main/not-found.html", status=404)


