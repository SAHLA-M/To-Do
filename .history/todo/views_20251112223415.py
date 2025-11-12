from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addTask(request):
    p(request.POST['task'])
    return HttpResponse('thr do')