from django.contrib import admin
from Apps.Viajes.models import Viaje, Origen,Destino,MotivoViajes,ViajeMotivoViaje

# Register your models here.

class MembershipInline(admin.TabularInline):
    model = ViajeMotivoViaje
    extra = 1

class viajesAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)
    #list_display = ('numero_plazas')

class OrigenAdmin(admin.ModelAdmin):
    pass
class DestinoAdmin(admin.ModelAdmin):
    pass
class MotivoViajesAdmin(admin.ModelAdmin):
    pass
    


admin.site.register(Viaje, viajesAdmin)
admin.site.register(Origen, OrigenAdmin)
admin.site.register(Destino, DestinoAdmin)
admin.site.register(MotivoViajes, MotivoViajesAdmin)
