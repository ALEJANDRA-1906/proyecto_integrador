# Generated by Django 4.1 on 2022-09-21 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_eliminacion', models.DateTimeField(auto_now=True)),
                ('descripcion', models.CharField(max_length=100, unique=True, verbose_name='Descripcion')),
                ('alias', models.CharField(max_length=100, unique=True, verbose_name='Alias')),
                ('codigo_barra', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('stock_minimo', models.FloatField(default=0)),
                ('stock_maximo', models.FloatField(default=0)),
                ('foto', models.FileField(blank=True, null=True, upload_to='ventas/articulos/')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
                ('costo', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de Costo')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de Venta')),
                ('con_iva', models.BooleanField(default=True, verbose_name='Iva')),
                ('estado', models.BooleanField(default=True)),
                ('grupo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.grupo')),
                ('linea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.linea')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
                'ordering': ['descripcion'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_eliminacion', models.DateTimeField(auto_now=True)),
                ('ruc', models.CharField(max_length=13, unique=True)),
                ('nombres', models.CharField(max_length=200, unique=True)),
                ('direccion', models.TextField(blank=True, null=True, verbose_name='Dirección')),
                ('genero', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('telefonos', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('foto', models.FileField(blank=True, null=True, upload_to='ventas/clientes/')),
                ('estado', models.BooleanField(default=True)),
                ('ciudad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.ciudad')),
                ('pais', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.pais')),
                ('provincia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.provincia')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ('nombres',),
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('fecha_eliminacion', models.DateTimeField(auto_now=True)),
                ('forma_pago', models.CharField(choices=[('E', 'Efectivo'), ('C', 'Credito'), ('V', 'Paypal')], default='E', max_length=1)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('iva', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('estado', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='ventas.cliente')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'ordering': ('-fecha', 'cliente'),
            },
        ),
        migrations.CreateModel(
            name='FacturaDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('tasa_iva', models.FloatField(blank=True, default=0, null=True)),
                ('iva', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ventas.articulo')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ventas.factura')),
            ],
            options={
                'verbose_name': 'Factura Detalle',
                'verbose_name_plural': 'Factura Detalles',
                'ordering': ('factura',),
            },
        ),
    ]
