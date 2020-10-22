from django.contrib import admin

from core.models import Remember


@admin.register(Remember)
class RememberAdmin(admin.ModelAdmin):
    """Отображение модели Remember в админке, добавлено отображение полей для чтения в детальном просмотре"""
    readonly_fields = ('id', 'date_create',)
