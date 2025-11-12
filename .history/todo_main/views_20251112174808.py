from django.shortcuts import render,redirect
fro
def home(request):
    task=Tasks.objects.filter(is_compleated=True)
    return  render(request,'home.html')


