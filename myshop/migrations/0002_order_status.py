# Generated by Django 4.1.7 on 2023-03-20 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='Carrito', max_length=200, verbose_name='Estado'),
        ),
    ]