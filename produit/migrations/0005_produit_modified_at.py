# Generated by Django 4.1.1 on 2022-09-29 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0004_remove_produit_modfied_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='modified_at',
            field=models.DateTimeField(null=True),
        ),
    ]
