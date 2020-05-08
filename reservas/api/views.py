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
