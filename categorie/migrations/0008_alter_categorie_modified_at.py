# Generated by Django 4.1.1 on 2022-09-29 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorie', '0007_alter_categorie_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Date Mise Jour'),
        ),
    ]
