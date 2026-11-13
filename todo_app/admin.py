from django.contrib import admin
from .models import todo_User,Task
# Register your models here.

admin.site.register(todo_User)
admin.site.register(Task)