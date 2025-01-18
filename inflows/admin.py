from django.contrib import admin

from .models import Inflow


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'created_at', 'created_at',)
    search_fields = ('supplier__name', 'product__name',)
