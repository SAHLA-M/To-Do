from django.conf.shortcuts import Http
def home(request):
    return  HttpResponse('home page is good')