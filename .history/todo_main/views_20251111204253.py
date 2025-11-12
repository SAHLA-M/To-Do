from django.conf.shortcuts import HttpResponse
def home(request):
    return  HttpResponse('home page is good')