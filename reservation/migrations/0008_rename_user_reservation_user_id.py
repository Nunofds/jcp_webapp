# Generated by Django 4.1.1 on 2022-10-15 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0007_alter_reservation_date_alter_reservation_hour'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='user',
            new_name='user_id',
        ),
    ]
