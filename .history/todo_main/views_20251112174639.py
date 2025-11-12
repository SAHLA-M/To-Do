from django.shortcuts import render,redirect

def home(request):
    task=Tasks.o
    return  render(request,'home.html')


