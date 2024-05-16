from django.contrib import admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin

from .models import Picture


@admin.register(Picture)
class PictureAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'get_image')
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width=50 height=60>")
