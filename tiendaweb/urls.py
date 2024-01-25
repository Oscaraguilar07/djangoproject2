from django.contrib import admin
from django.urls import path
from tiendaweb.views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('registro/', registro_views, name='registro'),
    path('admin/', admin.site.urls),

]

