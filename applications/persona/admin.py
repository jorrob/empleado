from django.contrib import admin

from .models import Empleado, habilidades


admin.site.register(habilidades)
# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job',
        'departamento',
        'full_name',
        'id',

    )

    def full_name (self,obj):
        print(obj.first_name)
        return obj.first_name + '- '+ obj.last_name

    #buscardor
    search_fields = ('first_name','last_name',)
    list_filter = ('departamento','job','habilidades',)
    #solo funciona de muchos a muchos
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)