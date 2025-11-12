from django.shortcuts import render,redirect

def home(request):
    task=Tasks.objects.filter(isc)
    return  render(request,'home.html')


