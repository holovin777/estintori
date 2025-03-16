from django.contrib import admin
from .models import FireExtinguisher, Owner

@admin.register(FireExtinguisher)
class FireExtinguisherAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'type', 'net_weight', 'owner', 'manufacture_date', 
        'revision_expiry_date', 'test_expiry_date', 'next_maintenance_date', 
        'location', 'active'
    )
    list_filter = ('type', 'active', 'revision_expiry_date', 'test_expiry_date', 'owner')
    search_fields = ('code', 'location', 'owner__name')
    ordering = ('revision_expiry_date', 'test_expiry_date')
