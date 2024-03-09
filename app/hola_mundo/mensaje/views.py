from django.shortcuts import render

def mensaje(request):
    calificaciones = [
        {'materia':'SO Linux','calificacion':10},
        {'materia':'Framewroks','calificacion':11},
        {'materia':'Testing','calificacion':8},
        {'materia':'Deployement','calificacion':9},
        {'materia':'Ética','calificacion':7},
        {'materia':'TSP','calificacion':10},
    ]
    context = {
        'nombre' : 'Oscar',
        'semestre' : 8,
        'materias' : [
            'SO Linux',
            'Frameworks',
            'Testing',
            'Deployment',
            'Ética',
            'TSP,'
        ],
        'calificaciones': calificaciones
    }
    return render(request, 'mensaje.html', context)

def despedida(request):
    
    context = {
        'nombre' : 'Oscar',
    }
    return render(request, 'despedida.html', context)

def hola(request,id):
    print(request)
    print(id)
    context = {
        'id' : id
    }
    return render(request, 'protocolo.html', context)

def mensaje2(request):
    
    context = {
        'nombre' : 'Oscar',
    }
    return render(request, 'mensaje.html', context)


def cadena(request, nombre):
    context = {
        'nombre' : nombre,
    }
    return render(request, 'protocolo.html', context)

def id_cadena(request, nombre, id):
    context = {
        'nombre' : nombre,
        'id' : id
    }
    return render(request, 'protocolo.html', context)

def login(request):
    context = {'valido':False}
    context = {'primero':True}
    if request.method == 'POST':
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print(request.POST)
        context['username'] =username
        context['valido'] = valida_usuario(username,password)
        context['primero'] = False
        
    return render(request, 'formulario.html', context)

def valida_usuario(username,password):
    if username == 'admin' and password == 'admin123':
        return True
    return False 

def calculadora(request):
    context = {'valido':False}
    if request.method == 'POST':
        primerNumero = request.POST.get("primerNumero",None)
        segundoNumero = request.POST.get("segundoNumero",None)
    
        context['respuesta'] =(int)(primerNumero)+ (int)(segundoNumero)
        context['valido'] = True
        
    return render(request, 'calculadora.html', context)

def calculadora2(request):
    context = {'valido':False}
    if request.method == 'POST':
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('resultado', 0))
        operacion = request.POST.get('operacion')
        resultado = opera1(operacion,num1,num2)
        return render(request, 'calculadora2.html', {'resultado': resultado})

    return render(request, 'calculadora2.html', {'resultado': 0})

def opera1(operador, a, b):
    if operador == '+':
        return a + b
    elif operador == '-':
        return a - b
    elif operador == 'X':
        return a * b
    elif operador == '/':
        return a / b
    else:
        return None
