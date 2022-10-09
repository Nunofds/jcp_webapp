# Generated by Django 4.1.1 on 2022-10-09 13:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_remove_contact_whatched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, null=True, validators=[django.core.validators.RegexValidator('^/[a-zA-Z]+( )$/')], verbose_name='Nom Contact'),
        ),
    ]