from django.shortcuts import render
fro

# Create your views here.
def addTask(request):
    print(request.POST)
    return HttpResponse('thr do')