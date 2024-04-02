from django.contrib import admin

from .models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'category_id')
    search_fields = ('product_id', 'category_id')


admin.site.register(ProductCategory, ProductCategoryAdmin)

admin.site.register(Product, ProductAdmin)
