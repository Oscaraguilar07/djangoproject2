from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm
from django.views import View
import MySQLdb


def index (request):
    return render (request,'index.html',{
    
    })

def login_views(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')

        user = authenticate(username=usuario, password=contraseña)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no válido')

    return render(request, 'login.html', {
        
    })
    
def registro_views(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Autenticar al usuario después del registro
            login(request, user)
            messages.success(request, '¡Registro exitoso! Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Error en el formulario. Por favor, corrige los errores.')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})



def mostrar_productos(request):

    conexion = MySQLdb.connect(
        host='localhost',
        user='root',
        password='',
        db='tienda_virtual'
    )


    cursor = conexion.cursor()


    cursor.execute('SELECT * FROM productos')


    productos = cursor.fetchall()

    # Cierra la conexión
    cursor.close()
    conexion.close()


    return render(request, 'index.html', {'productos': productos})
