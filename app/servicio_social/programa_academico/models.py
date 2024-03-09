from django.db import models

# Create your models here.


class UnidadAcademica(models.Model):
    nombre = models.CharField(max_length = 150)
    descripcion = models.TextField('Descripcion')

    def __str__(self):
        return self.nombre

class ProgramaAcademico(models.Model):
    nombre = models.CharField(max_length = 150)
    descripcion = models.TextField('Descripcion')
    unidad_academica = models.ForeignKey("programa_academico.UnidadAcademica",verbose_name ='Unidad Academica', on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.nombre