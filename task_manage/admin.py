from django.contrib import admin
from . import models

class TaskInline(admin.StackedInline):
    model=models.Task
    extra=1

# Register your models here.
@admin.register(models.Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display=['email']
    inlines=[TaskInline]

@admin.register(models.Student)
class AdminStudent(admin.ModelAdmin):
    list_display=['email']

@admin.register(models.Task)
class AdminTask(admin.ModelAdmin):
    list_display=['task_name']
