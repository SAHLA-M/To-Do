from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.Model)
admin.site.register(Task)
