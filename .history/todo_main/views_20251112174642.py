from django.shortcuts import render,redirect

def home(request):
    task=Tasks.objects
    return  render(request,'home.html')


