from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_unidades_academicas, name='lista_unidades'),
    path('nueva/', views.nueva_unidad , name='nueva_unidad'),
    path('nueva-ajax/', views.nueva_unidad_ajax , name='nueva_unidad_ajax'),
    path('editar/<int:id>', views.editar_unidad , name='editar_unidad'),
    path('eliminar/<int:id>', views.eliminar_unidad, name='eliminar_unidad'),
    
    path('lista_programa/', views.lista_programas_academicos, name='lista_programas_academicos'),
    path('nuevo_programa/', views.nuevo_programa , name='nuevo_programa'),
    path('editar_programa/<int:id>', views.editar_programa , name='editar_programa'),
    path('eliminar_programa/<int:id>', views.eliminar_programa, name='eliminar_programa')
]
