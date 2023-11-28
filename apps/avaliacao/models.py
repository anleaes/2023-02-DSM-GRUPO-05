from django.db import models

# Create your models here.

class avaliacao(models.Model):
    peso = models.TextField('Peso', max_length=50)
    altura = models.TextField('Altura', max_length=100)
    medidas_corporais = models.TextField('Medida Corporal', max_length=100)
    percentual_gordura = models.TextField('Percentural de gordura', max_length=100)
    
    class Meta:
        verbose_name = 'avaliacao'
        verbose_name_plural = 'Avaliacoes'
        ordering =['id']

    def __str__(self):
        return self.name