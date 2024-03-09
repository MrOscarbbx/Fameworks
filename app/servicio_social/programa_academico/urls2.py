from django.urls import path
from . import views

urlpatterns = [    
    path('lista/', views.lista_programas_academicos, name='lista_programas_academicos'),
    path('nuevo/', views.nuevo_programa , name='nuevo_programa'),
    path('editar/<int:id>', views.editar_programa , name='editar_programa'),
    path('eliminar/<int:id>', views.eliminar_programa, name='eliminar_programa')
]
