
from django.contrib import admin
from django.urls import path, include
from programa_academico.views import bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('unidades/', include('programa_academico.urls')),
    path('programas/', include('programa_academico.urls2')),
    path('',bienvenida, name='bienvenida')
]
