from django.conf.shortcuts import HttpRes
def home(request):
    return  HttpResponse('home page is good')