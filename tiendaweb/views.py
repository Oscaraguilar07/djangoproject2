from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# views.py
# views.py
from django.shortcuts import render
from .models import Producto

def index(request):
    print("Renderizando la vista index")
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})








def index (request):
    return render (request,'index.html',{
    
    })

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'Login.html',{

    })
    
@login_required    
def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')
    
@csrf_protect    
def registro_views(request):
    form = RegisterForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        
        user = User.objects.create_user(username, email, password)
        if user:
            login(request, user)
            messages.success(request, 'usuario creado exitosamente')
            return redirect('index')
            
        print(username)
        print(email)
        print(password)
    
    return render(request, 'Registro.html',{
        'form': form
    })

def index(request):
    return render (request,"index.html")



