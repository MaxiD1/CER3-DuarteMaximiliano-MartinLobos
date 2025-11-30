from django.contrib import admin
from .models import libro

@admin.register(libro)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn')

    '''
    def mostrar_num_inscritos(self, obj):
        return f"{obj.total_inscritos()} / {obj.capacidad}"
    
    def dinero(self,obj):
        return(obj.precio * obj.total_inscritos())

    mostrar_num_inscritos.short_description = 'Inscritos'

    dinero.short_description = 'Dinero acumulado'
    '''
