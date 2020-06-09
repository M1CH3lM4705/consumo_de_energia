from django.db import models
from ambientes.models import Ambiente

# Create your models here.

class AparelhoManager(models.Manager):
    
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(potencia__icontains=query))

class Aparelho(models.Model):
    name = models.CharField(verbose_name='Nome do aparelho', max_length=100)
    slug = models.SlugField(verbose_name='Atalho')
    potencia = models.IntegerField(verbose_name='Potencia em watts', null=True, blank=True)
    tempo = models.IntegerField(verbose_name='Tempo sugerido',null=True, blank=True)
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
    
    aparelho = models.ForeignKey(Aparelho, verbose_name='Aparelho', related_name='aparelho_ambiente', on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, verbose_name='Ambiente', related_name='ambiente_aparelho', on_delete=models.CASCADE)
    status = models.IntegerField('Tempo sugerido', choices=STATUS_CHOICES, default=2, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    
    class Meta:
        db_table = 'aparelho_ambiente'
        verbose_name = 'Aparelho e Ambiente'
        verbose_name_plural = 'Aparelhos e Ambientes'
        unique_together = (('aparelho', 'ambiente'))