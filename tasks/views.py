from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_tasks(request):
    return HttpResponse("task list")