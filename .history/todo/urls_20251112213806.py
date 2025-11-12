from django.urls import path
from . import vie

urlpatterns = [
    path('addTask/',views.addTask,name='a')
]
