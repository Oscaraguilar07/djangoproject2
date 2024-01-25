from django.contrib import admin
from django.urls import path
from tiendaweb.views import *

# urls.py

from .views import index

urlpatterns = [
    path('', index, name='index'),
]


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registro/', registro_views, name='registro'),
    path('admin/', admin.site.urls),

]

