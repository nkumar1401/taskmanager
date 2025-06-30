from django.contrib import admin

# Register your models here.
from .models import Task

admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)