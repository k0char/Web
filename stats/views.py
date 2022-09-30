from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Witaj na stronie ze statystykami")
def zibi(request):
    return HttpResponse("Staty zibiego:\ngole: 1\nasysty: 2\n mecze: 4")
def mati(request):
    return HttpResponse("Staty matiego:\ngole: 3\nasysty: 4\n mecze: 7") 