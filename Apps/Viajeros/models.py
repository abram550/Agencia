from django.db import models

# Create your models here.


class Viajeros(models.Model):
    dni = models.CharField(max_length=20,verbose_name="Ingrese el DNI del Viajero")
    nombreViajeros = models.CharField(max_length=100, verbose_name="Ingrese el Nombre del Viajero")
    direccionViajeros = models.CharField(max_length=100, verbose_name="Ingrese la Direccion del Viajero")
    telefonoViajeros = models.CharField(max_length=12, verbose_name="Ingrese el Telefono del Viajero")

    def __str__(self):
        return self.dni

    class Meta:
        verbose_name = "viajeros"
        verbose_name_plural = "viajeros"

class ReferenciaFamiliar(models.Model):
    
    nombre = models.CharField(max_length=100, verbose_name="Ingrese el Nombre del familiar")
    apellido = models.CharField(max_length=100, verbose_name="Ingrese el apellido del familiar")
    direccion = models.CharField(max_length=200, verbose_name="Ingrese el direccion del familiar")
    telefono = models.CharField(max_length=20, verbose_name="Ingrese el telefono del familiar")
    dni_viajero = models.ForeignKey(Viajeros,null=True,blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.dni_viajero.dni})"
    
    class Meta:
        verbose_name = "referencia Familiar"
        verbose_name_plural = "referencia Familiar"
