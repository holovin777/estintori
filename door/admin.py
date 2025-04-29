from django.contrib import admin
from .models import FireDoor

@admin.register(FireDoor)
class FireDoorAdmin(admin.ModelAdmin):
    list_display = ('code', 'location', 'installation_date', 'next_maintenance_date', 'active', 'owner')
    list_filter = ('active', 'owner')
    search_fields = ('code', 'location')
