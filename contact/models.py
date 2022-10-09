from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db import models


class Contact(models.Model):
    name = models.CharField('Nom Contact', max_length=255, null=True,
    )
    email = models.EmailField('Email Contact', null=True)
    phone = models.CharField('Telephone Contact', max_length=20, null=True)
    subject = models.CharField('Sujet Message', max_length=100, null=True)
    message = models.TextField('Message', null=True)
    created_at = models.DateTimeField('Date Creation', auto_now_add=True, null=True)

    def __str__(self):
        return self.name

