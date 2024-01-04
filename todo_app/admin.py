from django.contrib import admin
from todo_app.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'user')

admin.site.register(Task)