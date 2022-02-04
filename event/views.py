from django.shortcuts import render, HttpResponse


from .models import BuatEvent, DaftarEvent
# Create your views here.

def index(request):
    return HttpResponse('<h1>Home</h1>')


def buatEvent(request):
    