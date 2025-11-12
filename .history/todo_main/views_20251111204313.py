from django.shortcuts import HttpResponse,render,redire
def home(request):
    return  HttpResponse('home page is good')