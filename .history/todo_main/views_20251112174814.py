from django.shortcuts import render,redirect
from todo
def home(request):
    task=Tasks.objects.filter(is_compleated=True)
    return  render(request,'home.html')


