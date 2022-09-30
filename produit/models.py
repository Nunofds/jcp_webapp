from django.db import models
from categorie.models import Categorie


class Produit(models.Model):
    name = models.CharField('Nom Produit', max_length=100, null=True)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    price = models.FloatField('Prix Produit', null=True)
    description = models.TextField('Description Produit', null=True)
    image = models.ImageField('Image Produit', null=True)
    created_at = models.DateTimeField('Date Creation', auto_now_add=True, null=True)
    modified_at = models.DateTimeField('Date Mise Jour', auto_now=True, null=True)

    def __str__(self):
        return self.name


