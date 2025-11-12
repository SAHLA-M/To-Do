from django.shortcuts import HttpResponse,render,redirect
def home(request):
    return  rnd('home page is good')