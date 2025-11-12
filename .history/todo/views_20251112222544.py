from django.shortcuts import render
from d

# Create your views here.
def addTask(request):
    print(request.POST)
    return HttpResponse('thr do')