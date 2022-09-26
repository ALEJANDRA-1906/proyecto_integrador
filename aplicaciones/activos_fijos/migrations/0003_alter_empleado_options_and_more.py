# Generated by Django 4.1 on 2022-09-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos_fijos', '0002_empleado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ('nombre',), 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='nombres',
            new_name='apellido',
        ),
        migrations.RemoveField(
            model_name='activo',
            name='descripcion',
        ),
        migrations.AddField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(default=2, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]