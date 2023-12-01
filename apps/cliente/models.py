from django.db import models
from nivel.models import nivel
from plano.models import plano

# Create your models here.

class cliente(models.Model):
    primeiro_nome = models.CharField('Nome', max_length=50)
    ultimo_nome = models.CharField('Sobrenome', max_length=100) 
    endereço = models.CharField('Endereco', max_length=200)   
    telefone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    genero = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    cliente_nivel = models.ManyToManyField(nivel)
    cliente_plano = models.ManyToManyField(plano)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering =['id']

    def __str__(self):
        return self.primeiro_nome



class clientenivel(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    nivel = models.ForeignKey(nivel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'nivel'
        verbose_name_plural = 'niveis'
        ordering =['id']

    def __str__(self):
        return self.nivel
    
class clienteplano(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    plano = models.ForeignKey(plano, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'plano'
        verbose_name_plural = 'planos'
        ordering =['id']

    def __str__(self):
        return self.name