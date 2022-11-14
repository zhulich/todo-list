from django.contrib import admin

from todo.models import Task, Tag


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("content",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
