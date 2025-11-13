from django.shortcuts import render,redirect
from todo.models import Task
def home(request):
    activtask=Task.objects.filter(is_compleated=False).order_by('-updated_at')
    context={
        'actask':task
    }
    return  render(request,'home.html',context)


