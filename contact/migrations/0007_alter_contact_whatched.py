# Generated by Django 4.1.1 on 2022-09-29 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_alter_contact_whatched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='whatched',
            field=models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=20, null=True, verbose_name='TRAITEE ?'),
        ),
    ]
