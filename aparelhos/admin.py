from django.contrib import admin
from aparelhos.models import Aparelho

# Register your models here.

class AparelhoAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'potencia', 'tempo', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Aparelho, AparelhoAdmin)