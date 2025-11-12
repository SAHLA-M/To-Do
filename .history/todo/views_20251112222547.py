from django.shortcuts import render
from django.

# Create your views here.
def addTask(request):
    print(request.POST)
    return HttpResponse('thr do')