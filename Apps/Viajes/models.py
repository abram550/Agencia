from django.db import models
from Apps.Viajeros.models import Viajeros
from django.utils.timezone import now



class Destino(models.Model):
    nombre_destino = models.CharField(max_length=100, verbose_name = "Ingrese el Destino")

    def __str__(self):
        return self.nombre_destino
    
    class Meta:
        verbose_name = "destino"
        verbose_name_plural = "destino"
    
class Origen(models.Model):
    nombre_origen = models.CharField(max_length=100, verbose_name = "Ingrese el Origen")
    
    def __str__(self):
        return self.nombre_origen
    
    class Meta:
        verbose_name = "origen"
        verbose_name_plural = "origen"


class Viaje(models.Model):
    numero_plazas = models.CharField(max_length=10, verbose_name = "Ingrese el Numero plazas")
    fecha_viaje = models.DateField(default=now,verbose_name = "Ingrese la fecha de viaje")
    destino = models.ForeignKey(Destino,null=True,
                                    blank=True, on_delete=models.CASCADE)
    origen = models.ForeignKey(Origen,null=True,
                                    blank=True, on_delete=models.CASCADE)
    viajeros = models.ForeignKey(Viajeros,null=True,
                                    blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.origen.nombre_origen} - {self.destino.nombre_destino}"
    
    class Meta:
            verbose_name = "Viaje"
            verbose_name_plural = " Viaje"