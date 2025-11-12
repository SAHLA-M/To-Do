from django.shortcuts import HttpResponse,render,redirect
def home(request):
    return  HttpResponse('home page is good')