from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('mark_as_done/<int:pk>/',views.mark_as_done, name='mark_as_done'),
    path('undone/<int:pk>/',views.undone,name="undone")
    path('deleteTask/<int:pk>/',views.deleteTask)

]
