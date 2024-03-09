from django.shortcuts import render, redirect
from .models import UnidadAcademica,ProgramaAcademico
from .forms import FormUnidadAcademica,FormProgramaAcademico,FormFiltrosPrograma
from django.http import JsonResponse
# Create your views here.

def lista_unidades_academicas(request):
    context = {"unidades" : UnidadAcademica.objects.all()}
    return render(request,'lista_unidades.html',context)

def eliminar_unidad(request,id):
    unidad = UnidadAcademica.objects.get(id=id)
    programas = ProgramaAcademico.objects.filter(unidad_academica=unidad)
    for programa in programas:
        programa.delete()
    unidad.delete()
    return redirect('lista_unidades')

def editar_unidad(request,id):
    unidad = UnidadAcademica.objects.get(id=id)
    form = FormUnidadAcademica(instance=unidad)
    if request.method == 'POST':
        form = FormUnidadAcademica(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            return redirect('lista_unidades')
        else:
            form = FormUnidadAcademica(instance=unidad)
    context = {'form':form}
    return render(request,'editar_unidad.html',context)

def nueva_unidad(request):
    if request.method == 'POST':
        form = FormUnidadAcademica(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_unidades')
        else:
            form = FormProgramaAcademico()

    context = {'form' : form}
    return render(request,'nueva_unidad.html',context) 

def nueva_unidad_ajax(request):
    if request.method == 'POST':
        form = FormUnidadAcademica(request.POST)
        if form.is_valid():
            unidad = form.save()
            unidades= list(UnidadAcademica.objects.all().values())
            response ={
                'ok' : 'Se guardo con exi6o',
                'unidades': unidades,
                'unidad' : unidad.id
            }
            return JsonResponse(response,safe=False) 
        else:
            return JsonResponse({'error' : f"Metodo mo validacion : {form.errors}" }, safe=False)
    else:
        return JsonResponse({'error' : 'Metodo mo Permitido'}, safe=False)

####################################################################


def lista_programas_academicos (request):
    programas = ProgramaAcademico.objects.all()
    print(programas.query)
    form = FormFiltroPrograma()
    context = {"programas" : programas}
    return render(request,'lista_programas_academicos.html',context)

def nuevo_programa (request):
    form = FormProgramaAcademico()
    formUnidad = FormUnidadAcademica()
    if request.method == 'POST':
        form = FormProgramaAcademico(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_programas_academicos')
        else:
            form = FormProgramaAcademico()
    context = {'form' : form, 'form_unidad' : formUnidad}
    return render(request,'nuevo_programa.html',context)

def editar_programa (request,id):
    programa = ProgramaAcademico.objects.get(id=id)
    form = FormProgramaAcademico(instance=programa)
    if request.method == 'POST':
        form = FormProgramaAcademico(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect('lista_programas_academicos')
        else:
            form = FormProgramaAcademico(instance=programa)
    context = {'form':form}
    return render(request,'editar_programa.html',context)

def eliminar_programa (request,id):
    programa = ProgramaAcademico.objects.get(id=id)
    programa.delete()
    return redirect('lista_programas_academicos')

def bienvenida (request):
    return render(request,'bienvenida.html')