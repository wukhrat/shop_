from django.contrib import admin

from .models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')


admin.site.register(Shop, ShopAdmin)
