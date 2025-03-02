from django.contrib import admin
from .models import Task


@admin.register(Task)
class FolderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'created_at'
    )
