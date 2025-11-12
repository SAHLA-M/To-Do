from django.shortcuts import render,redirect

def home(request):
    task=Tasks.obj
    return  render(request,'home.html')


