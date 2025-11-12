from django.shortcuts import render,r
from django.http import HttpResponse
from . models import Task
# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('thr do')