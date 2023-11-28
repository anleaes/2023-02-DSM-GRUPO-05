# Generated by Django 4.1 on 2023-11-28 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.TextField(max_length=50, verbose_name='Peso')),
                ('altura', models.TextField(max_length=100, verbose_name='Altura')),
                ('medidas_corporais', models.TextField(max_length=100, verbose_name='Medida Corporal')),
                ('percentual_gordura', models.TextField(max_length=100, verbose_name='Percentural de gordura')),
            ],
            options={
                'verbose_name': 'avaliacao',
                'verbose_name_plural': 'Avaliacoes',
                'ordering': ['id'],
            },
        ),
    ]