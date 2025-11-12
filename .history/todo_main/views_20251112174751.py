from django.shortcuts import render,redirect

def home(request):
    task=Tasks.objects.filter(is_co)
    return  render(request,'home.html')


