"""
URL configuration for ProyectoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProyectoDjango.views import saludo, nombre, dia_de_hoy, dia_de_hoy_personalizado, probando_template, probando_template_variables, usando_loader

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',saludo),
    path('nombre/',nombre),
    path('dia/',dia_de_hoy),
    path('dia/<personalizado>', dia_de_hoy_personalizado),
    path('template/',probando_template),
    path('template_variables/',probando_template_variables),
    path('template_variables_loader/',usando_loader)
]
