from django.contrib import admin
from .models import Categorie


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'modified_at')
    search_fields = ['name']


admin.site.register(Categorie, CategorieAdmin)

