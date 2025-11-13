from django.shortcuts import render,redirect
from django.http import HtvtpResponse
from . models import Task
from todo_main import 

# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')