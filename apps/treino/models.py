from django.db import models
from exercicio.models import exercicio

# Create your models here.

class treino(models.Model):
    name = models.CharField('Nome', max_length=50)
    descricao = models.CharField('descrição', max_length=100) 
    nivel_dificuldade = models.CharField('Dificuldade', max_length=200)
    treinoexercicio = models.ManyToManyField(exercicio)

    class Meta:
        verbose_name = 'treino'
        verbose_name_plural = 'treinos'
        ordering =['id']

    def __str__(self):
        return self.name


class treinoexercicio(models.Model):
    exercicio = models.ForeignKey(exercicio, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Exercicio'
        verbose_name_plural = 'Exercicios'
        ordering =['id']

    def __str__(self):
        return self.name