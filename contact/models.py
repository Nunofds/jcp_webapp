from django.db import models


class Contact(models.Model):
    choices = (
        ('OUI', 'OUI'),
        ('NON', 'NON'),
    )
    name = models.CharField('Nom Contact', max_length=255, null=True)
    email = models.EmailField('Email Contact', null=True)
    phone = models.CharField('Telephone Contact', max_length=20, null=True)
    subject = models.CharField('Sujet Message', max_length=100, null=True)
    message = models.TextField('Message', null=True)
    # whatched = models.CharField('TRAITEE ?', max_length=20, null=True, choices=choices)
    created_at = models.DateTimeField('Date Creation', auto_now_add=True, null=True)

    def __str__(self):
        return self.name

