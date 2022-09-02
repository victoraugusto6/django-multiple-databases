from django.contrib import admin

from multiple_database.task.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name',)
