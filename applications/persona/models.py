from django.db import models
from applications.departamento.models import Departamento

#from ckeditor.fi import RichTextField
from ckeditor.fields import RichTextField

# Create your models here.

class habilidades (models.Model):
    habilidad = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleado'
        #ordena el texto
        #ordenig = ['name']
        
        #no se repitan los datos
        #unique_together = ('habilidad')

    def __str__(self):
        return str(self.id) + '-' + self.habilidad 

class Empleado (models.Model):
    #"" Modelo para Empleado
    
    job_choices = (
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','Otro'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombres Completops', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices= job_choices)
    #clave foranea departamento
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField (upload_to='empleado', blank=True, null=True)
    #Relacion muchos a muchos 
    habilidades = models.ManyToManyField(habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Persona'
        #ordena el texto
        #ordenig = ['name']
        
        #no se repitan los datos
        unique_together = ('first_name','last_name')



    def __str__(self):
        return   self.first_name + '-' + self.last_name 
