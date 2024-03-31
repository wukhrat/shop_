from django.contrib import admin

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')


admin.site.register(Category, CategoryAdmin)