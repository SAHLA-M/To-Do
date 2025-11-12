from django.urls import path
from . import v

urlpatterns = [
    path('addTask/',views.addTask,name='a')
]
