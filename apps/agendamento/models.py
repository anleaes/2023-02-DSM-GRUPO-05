from django.db import models
from instrutor.models import instrutor
from cliente.models import cliente

# Create your models here.

class agendamento(models.Model):
    data = models.CharField('Data', max_length=50)
    hora = models.CharField('Horário', max_length=100) 
    local = models.CharField('Endereco', max_length=200)   
    agendamento_instrutor = models.ManyToManyField(instrutor)
    agendamento_cliente = models.ManyToManyField(cliente)

    class Meta:
        verbose_name = 'agendamento'
        verbose_name_plural = 'agendamentos'
        ordering =['id']

    def __str__(self):
        return self.first_name