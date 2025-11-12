from django.shortcuts import render,redirect

def home(request):
    task=Tasks.objects.filter(is_com)
    return  render(request,'home.html')


