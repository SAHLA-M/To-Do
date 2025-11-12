from django.shortcuts import HttpResponse,render,redirect
def home(request):
    return  render(re'home page is good')