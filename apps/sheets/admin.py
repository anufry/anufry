from django.contrib import admin

from .models import *

@admin.register(Sheet)
class SheetAdmin(admin.ModelAdmin):
    list_display = ('title','slug',)
    search_fields = ['title']
    prepopulated_fields = {"slug": ("title",)}
