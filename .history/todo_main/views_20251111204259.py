from django.c.shortcuts import HttpResponse
def home(request):
    return  HttpResponse('home page is good')