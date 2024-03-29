# Generated by Django 3.0 on 2019-12-13 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('listaCompras', '0004_auto_20191213_1247'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='costoPreupuestado',
            new_name='costo_presupuestado',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='costoReal',
            new_name='costo_real',
        ),
        migrations.AlterField(
            model_name='producto',
            name='creador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.PerfilUsuario'),
        ),
    ]
