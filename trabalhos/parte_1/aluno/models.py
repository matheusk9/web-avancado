from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Matricula(models.Model):
    nome = models.CharField('Nome',max_length=100)
    periodo_de_ingresso = models.CharField('Período de Ingresso', max_length=10)
    nota = models.FloatField('Nota - Web Avançado')

    def __str__(self):
        return f'{self.nome}'