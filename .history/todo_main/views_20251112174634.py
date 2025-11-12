from django.shortcuts import render,redirect

def home(request):
    task=Task
    return  render(request,'home.html')


