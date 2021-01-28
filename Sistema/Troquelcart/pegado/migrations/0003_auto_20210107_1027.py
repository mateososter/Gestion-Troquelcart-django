# Generated by Django 3.1.4 on 2021-01-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegado', '0002_worker_net_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='nombre'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='nombre'),
        ),
    ]
