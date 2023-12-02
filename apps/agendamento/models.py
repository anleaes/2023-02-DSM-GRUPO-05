from django.db import models
from instrutor.models import instrutor
from cliente.models import cliente, clientenivel, clienteplano

# Create your models here.

class agendamento(models.Model):
    data = models.CharField('Data', max_length=50)
    hora = models.CharField('Hora', max_length=100) 
    local = models.CharField('Local', max_length=200)   
    agendamentoinstrutor = models.ManyToManyField(instrutor)
    agendamentoaluno = models.ManyToManyField(aluno)

class Meta:
        verbose_name = 'agendamento'
        verbose_name_plural = 'agendamentos'
        ordering =['id']

def __str__(self):
    return self.data

class agendamentoinstrutor(models.Model):
    agendamento = models.ForeignKey(agendamento, on_delete=models.CASCADE)
    instrutor = models.ForeignKey(instrutor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Instrutor'
        verbose_name_plural = 'Instrutores'
        ordering =['id']

    def __str__(self):
        return self.primeiro_nome


class agendamentoaluno(models.Model):
    agendamento = models.ForeignKey(agendamento, on_delete=models.CASCADE)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
        ordering =['id']

    def __str__(self):
        return self.primeiro_nome