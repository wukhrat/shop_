from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')


admin.site.register(Product, ProductAdmin)