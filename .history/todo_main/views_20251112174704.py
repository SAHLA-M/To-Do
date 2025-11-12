from django.shortcuts import render,redirect

def home(request):
    task=Tasks.objects.filter()
    return  render(request,'home.html')


