from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, "hello/index.html")
def zibi(request):
    return HttpResponse("Hello, Zibi")
def mati(request):
    return HttpResponse("Hello, mati")
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })