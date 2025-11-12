from django.shortcuts import render,redirect

def home(request):
    task=Tasks.objects.filter(is_)
    return  render(request,'home.html')


