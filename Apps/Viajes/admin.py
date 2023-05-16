from django.contrib import admin
from Apps.Viajes.models import Viaje, Origen,Destino

# Register your models here.


class viajesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Viaje, viajesAdmin)
admin.site.register(Origen, viajesAdmin)
admin.site.register(Destino, viajesAdmin)
