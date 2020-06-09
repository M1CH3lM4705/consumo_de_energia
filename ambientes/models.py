from django.db import models

# Create your models here.

class Ambiente(models.Model):

    name = models.CharField(verbose_name='Nome do ambiente', max_length=100, blank=True)
    slug = models.SlugField(verbose_name='Atalho')
    created_at = models.DateTimeField(verbose_name='Criado em',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'ambiente'
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'
        ordering = ['name']