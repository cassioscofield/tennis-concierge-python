from rest_framework.serializers import ModelSerializer

from reservas.models import Reserva

class ReservaSerializer(ModelSerializer):
  class Meta:
    model = Reserva
    fields = [
        'id',
        'status',
        'tipo',
        'valor',
        'duracao',
        'inicioEm',
        'fimEm'
    ]

class ReservaCreateSerializer(ModelSerializer):
  class Meta:
    model = Reserva
    fields = [
        'id',
        'tipo',
        'inicioEm',
        'fimEm'
    ]
  def create(self, validated_data):
        return Reserva.objects.create(**validated_data)