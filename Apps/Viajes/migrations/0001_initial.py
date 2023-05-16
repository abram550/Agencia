# Generated by Django 4.2.1 on 2023-05-16 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Viajeros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_destino', models.CharField(max_length=100, verbose_name='Ingrese el Destino')),
            ],
            options={
                'verbose_name': 'destino',
                'verbose_name_plural': 'destino',
            },
        ),
        migrations.CreateModel(
            name='Origen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_origen', models.CharField(max_length=100, verbose_name='Ingrese el Origen')),
            ],
            options={
                'verbose_name': 'origen',
                'verbose_name_plural': 'origen',
            },
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_plazas', models.CharField(max_length=10, verbose_name='Ingrese el Numero plazas')),
                ('fecha_viaje', models.DateField(verbose_name='Ingrese la fecha de viaje')),
                ('destino', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Viajes.destino')),
                ('origen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Viajes.origen')),
                ('viajeros', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Viajeros.viajeros')),
            ],
            options={
                'verbose_name': 'Viaje',
                'verbose_name_plural': ' Viaje',
            },
        ),
    ]
