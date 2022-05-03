from django.db import models

# Create your models here.

class Departamento (models.Model):
    name = models.CharField('Nombre', max_length=50)
    shortname = models.CharField('Nombre Corto', max_length=20, blank=True, null=True, unique=True)
    anulate = models.BooleanField('anulado', default=False)

    class Meta:
        #verbose_name = 'Mi Departamento'
        #verbose_name_plural = 'Areas de la Empresa'
        #ordena el texto
        #ordenig = ['name']
        #ordenig = ('name')
        #no se repitan los datos
        unique_together = ('name','shortname')

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.shortname 
