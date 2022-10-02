from django.contrib import admin
from .models import Produit


class ProduitAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'categorie',
        'description',
        'image',
    ]


admin.site.register(Produit, ProduitAdmin)


