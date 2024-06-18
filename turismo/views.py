from django.shortcuts import render
from .models import Servicio 
# Create your views here.

def index(request):
    return render(request, 'turismo/index.html')

def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'turismo/servicios.html', {'servicios': servicios})


