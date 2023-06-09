# Generated by Django 4.2.1 on 2023-05-16 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Viajeros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni', models.CharField(max_length=20, verbose_name='Ingrese el DNI del Viajero')),
                ('nombreViajeros', models.CharField(max_length=100, verbose_name='Ingrese el Nombre del Viajero')),
                ('direccionViajeros', models.CharField(max_length=100, verbose_name='Ingrese la Direccion del Viajero')),
                ('telefonoViajeros', models.CharField(max_length=12, verbose_name='Ingrese el Telefono del Viajero')),
            ],
            options={
                'verbose_name': 'viajeros',
                'verbose_name_plural': 'viajeros',
            },
        ),
        migrations.CreateModel(
            name='ReferenciaFamiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Ingrese el Nombre del familiar')),
                ('apellido', models.CharField(max_length=100, verbose_name='Ingrese el apellido del familiar')),
                ('direccion', models.CharField(max_length=200, verbose_name='Ingrese el direccion del familiar')),
                ('telefono', models.CharField(max_length=20, verbose_name='Ingrese el telefono del familiar')),
                ('dni_viajero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Viajeros.viajeros')),
            ],
            options={
                'verbose_name': 'referencia Familiar',
                'verbose_name_plural': 'referencia Familiar',
            },
        ),
    ]
