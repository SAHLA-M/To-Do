from django.shortcuts import render,redirect

def home(request):
    task=Tasks.objects.f
    return  render(request,'home.html')


