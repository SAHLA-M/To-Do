from django.shortcuts import render,redirect
from todo.models import Task
def home(request):
    task=Task.objects.filter(is_compleated=True).order_by
    context={
        'task':task
    }
    return  render(request,'home.html',context)


