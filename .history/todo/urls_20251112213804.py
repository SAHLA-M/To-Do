from django.urls import path
from . import 

urlpatterns = [
    path('addTask/',views.addTask,name='a')
]
