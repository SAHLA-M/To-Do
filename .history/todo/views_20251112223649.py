from django.shortcuts import render
from django.http import HttpResponse
from . models import Task
# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(task)
    return HttpResponse('thr do')