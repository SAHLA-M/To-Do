from django.shortcuts import render,redirect
from todo.models import Task
def home(request):
    activetask=Task.objects.filter(is_compleated=False).order_by('-updated_at')
    compleatedtask=Task.objects.filter(is_compleated=True).order_by('-updated_at')
    context={
        'activetask':activetask,
        'compleatedtask':compleatedtask
    }
    return  render(request,'home.html',context)


