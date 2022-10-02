from django.contrib import admin
from .models import Inventaire


class InventaireAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'created_at', 'modified_at')
    search_fields = ['product']


admin.site.register(Inventaire)

