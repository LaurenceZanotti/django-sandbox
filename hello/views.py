from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")


def laurence(request):
    return HttpResponse("Hello Laurence!")


def nadine(request):
    return HttpResponse("Hello Nadine!")