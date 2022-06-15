from django.shortcuts import render
from django.http import HttpResponse

def newsroom(request):
    return render(request, "newsroom/newsroom.html")


