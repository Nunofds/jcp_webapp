# Generated by Django 4.1.1 on 2022-10-09 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0017_alter_contact_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='Nom Contact'),
        ),
    ]
