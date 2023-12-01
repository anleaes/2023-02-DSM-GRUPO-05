from django.db import models

# Create your models here.

class exercicio(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    dificuldade = models.CharField('Dificuldade', max_length=50)
    area_desenvolvimento = models.CharField('Área de desenvolvimento', max_length=50)




    class Meta:
        verbose_name = 'exercicio'
        verbose_name_plural = 'exercicios'
        ordering =['id']

    def __str__(self):
        return self.name