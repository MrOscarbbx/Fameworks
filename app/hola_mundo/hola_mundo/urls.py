from django.contrib import admin
from django.urls import path
from mensaje import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', views.mensaje),
    path('hola2/', views.mensaje2),
    path('adios/', views.despedida),
    path('protocolo/<int:id>', views.hola),
    path('cadena/<str:nombre>', views.cadena),
    path('hola/', views.mensaje),
    path('id-cadena/<str:nombre>/<int:id>', views.id_cadena),
    path('login/', views.login),
    path('calculadora/', views.calculadora),
    path('calculadora2/', views.calculadora2),
]
