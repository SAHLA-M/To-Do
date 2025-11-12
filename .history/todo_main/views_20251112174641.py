from django.shortcuts import render,redirect

def home(request):
    task=Tasks.object
    return  render(request,'home.html')


