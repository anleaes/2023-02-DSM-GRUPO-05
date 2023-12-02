from django.db import models

# Create your models here.

class instrutor(models.Model):
    primeiro_nome = models.CharField('Nome', max_length=50)
    ultimo_nome = models.CharField('Sobrenome', max_length=100) 
    telefone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    especializacao = models.CharField('especializacao', max_length=100)
    
    class Meta:
        verbose_name = 'instrutor'
        verbose_name_plural = 'instrutor'
        ordering =['id']

    def __str__(self):
        return self.primeiro_nome