from django.shortcuts import render,redirect

def home(request):
    task=Tasks.objects.filt
    return  render(request,'home.html')


