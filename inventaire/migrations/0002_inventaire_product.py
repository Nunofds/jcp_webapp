# Generated by Django 4.1.1 on 2022-09-29 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_alter_produit_modfied_at'),
        ('inventaire', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventaire',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='produit.produit'),
        ),
    ]
