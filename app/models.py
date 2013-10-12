#coding=utf-8
from django.db import models
from django.utils.translation import ugettext as _


class Empresa(models.Model):
    razao_social = models.CharField(_('Razão Social'), max_length=200)
    nome_fantasia = models.CharField(_('Nome Fantasia'), null=True, blank=True, max_length=100)
    cnpj = models.CharField(_('Cnpj'), max_length=200)
    telefone = models.CharField(_('Telefone'), max_length=200)
    celular = models.CharField(_('Celular'), max_length=200)
    
    def __unicode__(self):
        return self.razao_social
      
    class Meta:        
        ordering = ["razao_social", "nome_fantasia", "cnpj"]
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")