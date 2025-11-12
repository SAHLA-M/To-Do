from django.shortcuts import HttpResponse,render,redirect
def home(request):
    return  render(request,'home page is good')