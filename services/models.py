from django.db import models


class Services(models.Model):
    name = models.CharField('Nom Service', max_length=100, null=True)
    image = models.ImageField('Image Service', upload_to='services', blank=True, null=True)
    desc = models.TextField('Description Service', null=True)
    created_at = models.DateTimeField('Date Creation', auto_now_add=True, null=True)
    modified_at = models.DateTimeField('Date Mise Jour', auto_now=True, null=True)

    def __str__(self):
        return self.name

