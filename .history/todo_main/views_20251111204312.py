from django.shortcuts import HttpResponse,render,redi
def home(request):
    return  HttpResponse('home page is good')