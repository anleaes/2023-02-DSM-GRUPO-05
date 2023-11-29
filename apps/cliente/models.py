from django.db import models
from avaliacao.models import avaliacao
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
    cliente_avaliacao = models.ManyToManyField(avaliacao, through='clienteavaliacao', blank=True)
    cliente_plano = models.ManyToManyField(plano, through='clienteplano', blank=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering =['id']

    def __str__(self):
        return self.first_name



class clientavaliacao(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    avaliacao = models.ForeignKey(avaliacao, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'avaliacao fisica'
        verbose_name_plural = 'avaliacoes fisicas'
        ordering =['id']

    def __str__(self):
        return self.avaliacao.name
    
class clienteplano(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    plano = models.ForeignKey(plano, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'plano'
        verbose_name_plural = 'planos'
        ordering =['id']

    def __str__(self):
        return self.plano.name