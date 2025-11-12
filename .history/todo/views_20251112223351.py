from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def addTask(request):
    print(request.POST['ta'])
    return HttpResponse('thr do')