# Generated by Django 4.1.1 on 2022-09-29 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_contact_whatched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='whatched',
            field=models.BooleanField(null=True, verbose_name='TRAITEE'),
        ),
    ]
