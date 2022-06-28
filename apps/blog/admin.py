from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','posted_at')
    # list_filter = ['root']
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}
    # readonly_fields = ('show_icon',)
    # form = CategoryForm
    fieldsets = (
        ('Заголовки', {
            'fields': ('title','slug','image')
        }),
        ('Основное', {
            'fields': ('teaser','text','posted_at')
        }),
        ('Meta', {
            'fields': ('meta_keywords','meta_description',)
        }),
    )

    # @mark_safe
    # def show_icon(self, obj):
    #     if not obj.icon:
    #         return '-'
    #     return obj.icon
    # show_icon.short_description = 'Иконка'
