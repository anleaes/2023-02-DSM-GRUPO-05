# Generated by Django 4.1 on 2023-11-29 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['id'], 'verbose_name': 'cliente', 'verbose_name_plural': 'clientes'},
        ),
    ]
