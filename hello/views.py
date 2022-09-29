from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world")
def zibi(request):
    return HttpResponse("Hello, Zibi")
def mati(request):
    return HttpResponse("Hello, mati")