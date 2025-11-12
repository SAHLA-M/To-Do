from django.shortcuts import render
from django.http import Http

# Create your views here.
def addTask(request):
    print(request.POST)
    return HttpResponse('thr do')