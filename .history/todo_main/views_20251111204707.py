from django.shortcuts import HttpResponse,render,redirect
def home(request):
    return  r('home page is good')