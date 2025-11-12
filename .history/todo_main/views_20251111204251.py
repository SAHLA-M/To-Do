from django.conf.shortcuts import HttpRespo
def home(request):
    return  HttpResponse('home page is good')