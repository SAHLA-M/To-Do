from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addTask(request):
    task=request.POST['task']
    Task.objects.create()
    return HttpResponse('thr do')