from django.contrib import admin
from cars.models import Carro, Marca

# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

class CarroAdmin(admin.ModelAdmin):
    list_display = ('id', 'modelo', 'marca', 'ano', 'km', 'cor', 'preco')
    list_filter = ('marca', 'ano', 'cor')

admin.site.register(Carro, CarroAdmin)
admin.site.register(Marca, MarcaAdmin)