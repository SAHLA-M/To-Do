from django.shortcuts import render,redirect
from todo.models import Task
def home(request):
    task=Task.objects.filter(is_compleated=True)
    context={
        t
    }
    return  render(request,'home.html')


