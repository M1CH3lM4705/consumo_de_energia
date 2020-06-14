from django.db import models
from ambientes.models import Ambiente
from django.db.models import signals
from django.urls import reverse
from consumo_de_energia.utils import slug_pre_save

# Create your models here.

class AparelhoManager(models.Manager):
    
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(potencia__icontains=query))

class Aparelho(models.Model):
    name = models.CharField(verbose_name='Nome do aparelho', max_length=100)
    slug = models.SlugField(verbose_name='Atalho', blank=True, max_length=100, unique=True)
    potencia = models.IntegerField(verbose_name='Potencia em watts', null=True, blank=True)
    tempo = models.IntegerField(verbose_name='Tempo sugerido', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    objects = AparelhoManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'aparelho'
        verbose_name = 'aparelho'
        verbose_name_plural = 'Aparelhos'
        ordering = ['name']


class Aparelho_Ambiente(models.Model):
    
    STATUS_CHOICES = (
        (1, 'minutos/dia'),
        (2, 'horas/dia'),
    )
    
    aparelho = models.ForeignKey(Aparelho, verbose_name='Aparelho', related_name='aparelhos', on_delete=models.deletion.DO_NOTHING)
    ambiente = models.ForeignKey(Ambiente, verbose_name='Ambiente', related_name='ambientes', on_delete=models.deletion.DO_NOTHING)
    status = models.IntegerField('Tempo sugerido', choices=STATUS_CHOICES, default=2, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        db_table = 'aparelho_ambiente'
        verbose_name = 'Aparelho e Ambiente'
        verbose_name_plural = 'Aparelhos e Ambientes'
        unique_together = (('aparelho', 'ambiente'))

#Signals

signals.pre_save.connect(slug_pre_save, sender=Aparelho)