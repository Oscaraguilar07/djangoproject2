from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
import MySQLdb


def index (request):
    return render (request,'index.html',{
        'message': 'wili😘😘'
    })

def login_views (request):
    return render (request,'login.html', {
 
    })
    
def registro_views (request):
    return render (request,'registro.html', {
 
    })



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
