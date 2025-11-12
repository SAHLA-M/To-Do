from django.shortcuts import render,redirect

def home(request):
    task=Tasks.objects.filter(isco)
    return  render(request,'home.html')


