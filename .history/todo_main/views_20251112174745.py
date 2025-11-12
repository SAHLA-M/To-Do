from django.shortcuts import render,redirect

def home(request):
    task=Tasks.objects.filter(isv)
    return  render(request,'home.html')


