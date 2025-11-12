from django.shortcuts import render
f

# Create your views here.
def addTask(request):
    print(request.POST)
    return HttpResponse('thr do')