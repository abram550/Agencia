from django.contrib import admin
from Apps.Viajeros.models import Viajeros,ReferenciaFamiliar

# Register your models here.


class viajerosAdmin(admin.ModelAdmin):
    pass



admin.site.register(Viajeros, viajerosAdmin)
admin.site.register(ReferenciaFamiliar, viajerosAdmin)