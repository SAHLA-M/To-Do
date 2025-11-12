from django.shortcuts import render
from django.ht

# Create your views here.
def addTask(request):
    print(request.POST)
    return HttpResponse('thr do')