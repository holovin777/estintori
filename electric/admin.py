from django.contrib import admin
from .models import ElectricPanel

@admin.register(ElectricPanel)
class ElectricPanelAdmin(admin.ModelAdmin):
    list_display = ('code', 'location', 'next_maintenance_date', 'active')
    list_filter = ('active', 'location')
    search_fields = ('code', 'location')
