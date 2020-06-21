from django.contrib import admin
from aparelhos.models import Aparelho, Aparelho_Ambiente

# Register your models here.

class AparelhoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'potencia', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

class Aparelho_AmbienteAdmin(admin.ModelAdmin):
    list_display = ['id','ambiente', 'aparelho']
    search_fields = ['ambiente', 'aparelho']

admin.site.register(Aparelho, AparelhoAdmin)
admin.site.register(Aparelho_Ambiente, Aparelho_AmbienteAdmin)