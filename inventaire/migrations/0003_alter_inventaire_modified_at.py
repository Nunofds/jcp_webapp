# Generated by Django 4.1.1 on 2022-09-29 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0002_inventaire_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventaire',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]