from django.shortcuts import render
from .models import Reserva

# Create your views here.
def find(request):
  reservas = Reserva.objects.all()
  return render(request, 'reservas.html', { 'reservas': reservas } )

def findById(request, id):
  reserva = Reserva.objects.get(id=id)
  return render(request, 'reserva.html', { 'reserva': reserva } )