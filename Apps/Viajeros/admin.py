from django.contrib import admin
from Apps.Viajeros.models import Viajeros,ReferenciaFamiliar

# Register your models here.

class viajerosAdmin(admin.ModelAdmin):

    list_display = ('dni','nombreViajeros','direccionViajeros')
    ordering = ('dni','nombreViajeros','direccionViajeros')
    search_fields = ('dni','nombreViajeros','direccionViajeros')
    list_filter = ('dni','nombreViajeros','direccionViajeros')


admin.site.register(Viajeros, viajerosAdmin)
admin.site.register(ReferenciaFamiliar)