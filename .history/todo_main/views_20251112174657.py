from django.shortcuts import render,redirect

def home(request):
    task=Tasks.objects.fil
    return  render(request,'home.html')


