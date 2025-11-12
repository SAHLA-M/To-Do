from django.conf.shortcuts import HttpRespon
def home(request):
    return  HttpResponse('home page is good')