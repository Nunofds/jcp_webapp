from django.db import models


class Categorie(models.Model):
    name = models.CharField('Nom Catégorie', max_length=50, null=True)
    created_at = models.DateTimeField('Date Création', auto_now_add=True, null=True)
    modified_at = models.DateTimeField('Date Mise Jour', auto_now=True, null=True)

    def __str__(self):
        return self.name

