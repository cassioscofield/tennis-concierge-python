from rest_framework.generics import (
  ListAPIView,
  RetrieveAPIView,
  UpdateAPIView,
  DestroyAPIView,
  CreateAPIView
)
from reservas.models import Reserva
from reservas.api.serializers import (
    ReservaSerializer,
    ReservaCreateSerializer
)

class ReservasListAPIView(ListAPIView):
  serializer_class = ReservaSerializer
  def get_queryset(self, *args, **kwargs):
    queryset_list = Reserva.objects.all()
    return queryset_list

class ReservasRetrieveAPIView(RetrieveAPIView):
  serializer_class = ReservaSerializer
  lookup_field = 'id'
  lookup_url_kwarg = 'id'
  def get_queryset(self, *args, **kwargs):
    queryset_list = Reserva.objects.all()
    return queryset_list

class ReservasDestroyAPIView(DestroyAPIView):
  serializer_class = ReservaSerializer
  lookup_field = 'id'
  lookup_url_kwarg = 'id'
  def get_queryset(self, *args, **kwargs):
    queryset_list = Reserva.objects.all()
    return queryset_list

class ReservasUpdateAPIView(UpdateAPIView):
  serializer_class = ReservaSerializer
  lookup_field = 'id'
  lookup_url_kwarg = 'id'
  def get_queryset(self, *args, **kwargs):
    queryset_list = Reserva.objects.all()
    return queryset_list

class ReservasCreateAPIView(CreateAPIView):
  serializer_class = ReservaCreateSerializer
  def get_queryset(self, *args, **kwargs):
    queryset_list = Reserva.objects.all()
    return queryset_list