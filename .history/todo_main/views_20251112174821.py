from django.shortcuts import render,redirect
from todo import models
def home(request):
    task=Tasks.objects.filter(is_compleated=True)
    return  render(request,'home.html')


