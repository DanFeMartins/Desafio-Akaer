from django.contrib.auth.models import User
from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    usuario = models.ManyToManyField(User, related_name='projetos')

    def __str__(self):
        return self.nom

class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    usuarios = models.ManyToManyField(User, related_name='empresas')
    projetos = models.ManyToManyField('Projeto', blank=True)
    

    def __str__(self):
        return self.nome