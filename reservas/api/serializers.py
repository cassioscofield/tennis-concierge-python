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
        'fimEm',
        'canceladoEm'
    ]

class ReservaCreateSerializer(ModelSerializer):
  class Meta:
    model = Reserva
    fields = [
        'id',
        'tipo',
        'status',
        'valor',
        'duracao',
        'duracao',
        'inicioEm',
        'fimEm'
    ]
  def create(self, validated_data):
        return Reserva.objects.create(**validated_data)