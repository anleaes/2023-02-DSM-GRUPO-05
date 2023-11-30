from django.db import models

# Create your models here.

class instrutor(models.Model):
    primeiro_nome = models.CharField('Nome', max_length=50)
    ultimo_nome = models.TextField('Sobrenome', max_length=100)
    telefone = models.TextField('Telefone', max_length=100)
    email = models.TextField('Email', max_length=100)
    especializacao = models.TextField('Especialização', max_length=100)
    
    class Meta:
        verbose_name = 'instrutor'
        verbose_name_plural = 'instrutores'
        ordering =['id']

    def __str__(self):
        return self.primeiro_nome