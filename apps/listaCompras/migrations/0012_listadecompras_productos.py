# Generated by Django 3.0 on 2019-12-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listaCompras', '0011_auto_20191219_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='listadecompras',
            name='productos',
            field=models.ManyToManyField(to='listaCompras.Producto'),
        ),
    ]
