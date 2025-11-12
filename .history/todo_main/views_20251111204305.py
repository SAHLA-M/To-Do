from django.shortcuts import HttpResponse,re
def home(request):
    return  HttpResponse('home page is good')