from django.contrib import admin
from ambientes.models import Ambiente

# Register your models here.

class AmbienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Ambiente, AmbienteAdmin)