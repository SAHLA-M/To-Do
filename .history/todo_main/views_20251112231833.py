from django.shortcuts import render,redirect
from todo.models import Task
def home(request):
    activetask=Task.objects.filter(is_compleated=False).order_by('-updated_at')
    cotask=Task.objects.filter(is_compleated=False).order_by('-updated_at')
    context={
        'activetask':activetask
    }
    return  render(request,'home.html',context)


