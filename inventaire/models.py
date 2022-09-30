from django.db import models
from produit.models import Produit


class Inventaire(models.Model):
    product = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField('Quantite Produits', null=True)
    created_at = models.DateTimeField('Date Creation', auto_now_add=True, null=True)
    modified_at = models.DateTimeField('Date Mise Jour', auto_now=True, null=True)

    def __str__(self):
        return self.product.name

