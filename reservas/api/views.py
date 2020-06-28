from rest_framework.generics import (
  ListAPIView,
  RetrieveAPIView,
  UpdateAPIView,
  DestroyAPIView,
  CreateAPIView
)
from reservas.api.serializers import (
    ReservaSerializer,
    ReservaCreateSerializer
)
from rest_framework.views import APIView
from reservas.models import Reserva
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from datetime import timedelta

class DisponibilidadeCustomViewSet(viewsets.ModelViewSet):

    def inverte_tipo(self, reserva):
      tipoInvertido = 'HARD'
      if reserva['tipo'] == 'HARD':
        tipoInvertido = 'SAIBRO'
      return {
        'tipo': tipoInvertido,
        'inicioEm': reserva['inicioEm'],
        'fimEm': reserva['fimEm']
      }

    def adiciona_hora_e_inverte_tipo(self, reserva, hours):
      result = self.adiciona_hora(reserva, hours)
      return self.inverte_tipo(result)

    def adiciona_hora(self, reserva, hours):
      inicioEmDate = datetime.datetime.strptime(reserva['inicioEm'], "%Y-%m-%dT%H:%M:%S%z")
      inicioEmDate = inicioEmDate + timedelta(hours=hours)
      inicioEmAlterado = inicioEmDate.isoformat()
      fimEmEmDate = datetime.datetime.strptime(reserva['fimEm'], "%Y-%m-%dT%H:%M:%S%z")
      fimEmEmDate = fimEmEmDate + timedelta(hours=hours)
      fimEmAlterado = fimEmEmDate.isoformat()
      return {
        'tipo': reserva['tipo'],
        'inicioEm': inicioEmAlterado,
        'fimEm': fimEmAlterado
      }

    def is_disponivel(self, reserva):
      queryset_list = Reserva.objects.filter(tipo=reserva['tipo'],inicioEm=reserva['inicioEm'],fimEm=reserva['fimEm'])
      queryset_count = queryset_list.count()
      if queryset_count < 1:
        return True
      return False

    def get_queryset(self, *args, **kwargs):
      return ''

    def verifica_disponibilidades(self, data):
      disponiveis = []
      tipoInverso = self.inverte_tipo(data)
      if self.is_disponivel(tipoInverso):
        disponiveis.append(tipoInverso)
      horaDeslocadaPraFrente = self.adiciona_hora(data, 1)
      if self.is_disponivel(horaDeslocadaPraFrente):
        disponiveis.append(horaDeslocadaPraFrente)
      horaDeslocadaPraTras = self.adiciona_hora(data, -1)
      if self.is_disponivel(horaDeslocadaPraTras):
        disponiveis.append(horaDeslocadaPraTras)
      horaDeslocadaPraFrenteETipoInvertido = self.adiciona_hora_e_inverte_tipo(data, 1)
      if self.is_disponivel(horaDeslocadaPraFrenteETipoInvertido):
        disponiveis.append(horaDeslocadaPraFrenteETipoInvertido)
      horaDeslocadaPraTrasETipoInvertido = self.adiciona_hora_e_inverte_tipo(data, -1)
      if self.is_disponivel(horaDeslocadaPraTrasETipoInvertido):
        disponiveis.append(horaDeslocadaPraTrasETipoInvertido)
      duasHorasDeslocadaPraFrente = self.adiciona_hora(data, 2)
      if self.is_disponivel(duasHorasDeslocadaPraFrente):
        disponiveis.append(duasHorasDeslocadaPraFrente)
      duasHorasDeslocadaPraTras = self.adiciona_hora(data, -2)
      if self.is_disponivel(duasHorasDeslocadaPraTras):
        disponiveis.append(duasHorasDeslocadaPraTras)
      return Response(disponiveis)
    
    @action(detail=True, methods=['post'])
    def post_disponibilidade(self, request):
      if self.is_disponivel(request.data):
        return Response([request.data])
      return self.verifica_disponibilidades(request.data)

    @action(detail=True, methods=['get'])
    def get_disponibilidade(self, request):
      now = datetime.now().replace(microsecond=0, second=0, minute=0)
      inicioEmDate = now + timedelta(hours=1)
      fimEmDate = now + timedelta(hours=2)
      reserva = {
        'tipo': 'HARD',
        'inicioEm': inicioEmDate.isoformat(),
        'fimEm': fimEmDate.isoformat()
      }
      disponiveis = []
      if self.is_disponivel(reserva):
        disponiveis.append(reserva)
      tipoInverso = self.inverte_tipo(reserva)
      if self.is_disponivel(tipoInverso):
        disponiveis.append(tipoInverso)
      return Response(disponiveis)

class ReservasListAPIView(ListAPIView):
  serializer_class = ReservaSerializer
  def get_queryset(self, *args, **kwargs):
    queryset_list = Reserva.objects.all()
    return queryset_list

class ReservasCreateAPIView(CreateAPIView):
  serializer_class = ReservaCreateSerializer
  def get_queryset(self, *args, **kwargs):
    queryset_list = Reserva.objects.all()
    return queryset_list

class ReservaAPIView(APIView):
  def get_object(self, id):
    try:
      return Reserva.objects.get(id=id)
    except Reserva.DoesNotExist:
      raise Http404

  def get(self, request, id, format=None):
    reserva = self.get_object(id)
    serializer = ReservaSerializer(reserva)
    return Response(serializer.data)

  def put(self, request, id, format=None):
    reserva = self.get_object(id)
    serializer = ReservaSerializer(reserva, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id, format=None):
    reserva = self.get_object(id)
    reserva.delete()
    serializer = ReservaSerializer(reserva)
    return Response(serializer.data)
