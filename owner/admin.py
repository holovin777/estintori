from django.contrib import admin
from .models import Owner

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'is_company')
    search_fields = ('name', 'email')
