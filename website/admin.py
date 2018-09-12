# coding=utf-8
from django.contrib import admin

from .models import Comercio, Gasto

class ComercioAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'created_at', 'updated_at']
    search_fields = ['name', 'slug']
    list_filter = ['created_at', 'updated_at']

class GastoAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'valor', 'datagasto', 'valor', \
            'comercio', 'created_at', 'modified_at']
    search_fields = ['name', 'slug','comercio__name']
    list_filter = ['created_at', 'modified_at']


admin.site.register(Comercio, ComercioAdmin)
admin.site.register(Gasto, GastoAdmin)
