from django.db import models
from django.db.models import signals
from django.urls import reverse
from consumo_de_energia.utils import slug_pre_save

# Create your models here.

class Ambiente(models.Model):

    name = models.CharField(verbose_name='Nome do ambiente', max_length=100, blank=True)
    slug = models.SlugField(verbose_name='Atalho', blank=True, unique=True, max_length=100)
    created_at = models.DateTimeField(verbose_name='Criado em',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ambientes:select_ambiente', kwargs={'slug':self.slug})
    
    class Meta:
        db_table = 'ambiente'
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'
        ordering = ['name']

#signals

signals.pre_save.connect(slug_pre_save, sender=Ambiente)