from django.contrib import admin
from .models import ProgramaAcademico
from .models import UnidadAcademica

# Register your models here.

admin.site.register(ProgramaAcademico)
admin.site.register(UnidadAcademica)