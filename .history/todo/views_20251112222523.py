from django.shortcuts import render

# Create your views here.
def addTask(request):
    print(request.POST)
    return HttpResponse