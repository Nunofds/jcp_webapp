from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    fullName = models.CharField('Nom Complet', max_length=250, null=True)
    adress = models.CharField('Adresse', max_length=100, null=True)
    zip_code = models.IntegerField('Code Postal', null=True)
    city = models.CharField('Vile', max_length=100, null=True)
    email = models.EmailField('Email', max_length=250, null=True)
    phone = models.CharField('Telephone', max_length=20, null=False)
    date = models.CharField('Date', max_length=20, null=True)
    hour = models.CharField('Heure', max_length=20, null=True)
    message = models.TextField('Message', null=True)
    accepted = models.BooleanField('Valide', null=True)
    created_at = models.DateTimeField('Date Creation', auto_now_add=True, null=True)
    modified_at = models.DateTimeField('Date Mise Jour', auto_now=True, null=True)

    def __str__(self):
        return self.fullName


