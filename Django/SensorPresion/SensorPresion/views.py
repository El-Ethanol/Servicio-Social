from SensorPresion.settings import TEMPLATES
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo(request):  
      
    return HttpResponse("Hola Mundo")

def adios(request):
    
    return HttpResponse("Adiós perro")

def fecha(request):
    
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")	
    docexterno=open("D:/Servicio Social/Django/SensorPresion/SensorPresion/Plantillas/Plantilla1.html")
    plt=Template(docexterno.read())
    docexterno.close()
    ctx=Context({"Fecha":date_time})
    nice=plt.render(ctx)
    
    return HttpResponse(nice)
    