# Generated by Django 4.1.1 on 2022-09-29 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0003_produit_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='modfied_at',
        ),
    ]
