from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def people(request):
    return HttpResponse("Name")