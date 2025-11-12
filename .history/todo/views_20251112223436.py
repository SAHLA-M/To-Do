from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addTask(request):
    task=request.POST['task']
    
    return HttpResponse('thr do')