# Generated by Django 4.1.1 on 2022-10-15 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_alter_reservation_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(max_length=20, null=True, verbose_name='Date'),
        ),
    ]
