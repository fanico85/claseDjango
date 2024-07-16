from django.http import HttpResponse #response
from datetime import datetime as dt  #fecha
from django.template import Template, Context # templates

def saludo(request):
    return HttpResponse("Hola mundillo! de Django")

def nombre(request):
    texto = "Soy Alejandro Ramirez<br>Cursando Python"
    return HttpResponse(texto)

def dia_de_hoy(rquest):
    dia = dt.now()
    dia = dia.strftime("%Y-%m-%d")
    texto = f"Hoy es:<br>{dia}"
    return HttpResponse(texto)

def dia_de_hoy_personalizado(request,personalizado):
    dia = dt.now()
    dia = dia.strftime("%Y-%m-%d")
    dia = dia[:-2] + personalizado
    texto = f"Hoy es:<br>{dia}"
    return HttpResponse(texto)

def probando_template(request):
    #abrimos el archivo html
    mi_html = open('./ProyectoDjango/plantillas/index.html')

    #creamos el temaplate haciendo uso de la clase Temaplate
    plantilla = Template(mi_html.read())

    #Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    #Creamos un contexto, por ahora vacio hasta aprender a utilizarlo
    mi_contexto = Context()

    #Terminamos de construir el temaplte renderizandolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)