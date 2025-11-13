from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect # <--- 1. Importa redirect

# 2. Función para redirigir
def redirect_to_api(request):
    return redirect('/api/') # Te manda a la URL de tu API

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('projects.urls')),
    path('', redirect_to_api), # <--- 3. Redirección automática
]