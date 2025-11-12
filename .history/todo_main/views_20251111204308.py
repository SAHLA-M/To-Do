from django.shortcuts import HttpResponse,render
def home(request):
    return  HttpResponse('home page is good')