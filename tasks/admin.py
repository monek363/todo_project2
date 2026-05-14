from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'complexity', 'priority', 'completed', 'created_at')
    list_filter = ('complexity', 'priority', 'completed', 'created_at')
    search_fields = ('title', 'description')
    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'description'),
        }),
        ('Параметри', {
            'fields': ('complexity', 'priority', 'color', 'completed'),
        }),
        ('Дати', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Task, TaskAdmin)