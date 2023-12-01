from django.db import models

# Create your models here.

class nivel(models.Model):
    nivel = models.TextField('nivel', max_length=50)
    
    class Meta:
        verbose_name = 'nivel'
        verbose_name_plural = 'nivel'
        ordering =['id']

    def __str__(self):
        return self.nivel