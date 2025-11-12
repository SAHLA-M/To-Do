from django.shortcuts import HttpResponse,render4
def home(request):
    return  HttpResponse('home page is good')