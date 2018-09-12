# coding=utf-8

from django.db import models
import datetime
from django.urls import reverse

class Comercio(models.Model):

    name = models.CharField('Comercio',max_length=100,null=False,blank=False)
    slug = models.SlugField('Identificador', max_length=100)
    created_at = models.DateTimeField('Criado em',auto_now_add=True,null=True)
    updated_at = models.DateTimeField('Atualizado em',auto_now=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Comércio'
        verbose_name_plural = 'Comércios'
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('website:lista_gastosPorComercio', kwargs={'slug': self.slug})

    objetos = models.Manager()

class Gasto(models.Model):

    name = models.CharField('Gastos',max_length=100,null=False,blank=False)
    slug = models.SlugField('Identificador', max_length=100)
    valor = models.CharField(max_length=100,null=False,blank=False)
    datagasto = models.DateField(default=datetime.datetime.today,null=True,blank=True)
    comercio = models.ForeignKey(Comercio,verbose_name='Comércio',on_delete=models.PROTECT)
    created_at = models.DateTimeField('Criado em',auto_now_add=True,null=True)
    modified_at = models.DateTimeField('Atualizado em',auto_now=True,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        ordering = ['-datagasto']

    objetos = models.Manager()
