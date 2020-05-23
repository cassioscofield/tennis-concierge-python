from django.db import models
from datetime import datetime
from django.utils import timezone
from rest_framework.exceptions import ValidationError

# Create your models here.
class Reserva(models.Model):

  def _valida_hora_quebrada(data):
    segundosInicio = data.second
    minutosInicio = data.minute
    if minutosInicio != 0 or segundosInicio != 0:
      raise ValidationError('nao pode ser hora quebrada')

  def _periodo_minimo(reserva, duracao):
    if (duracao < 60):
      raise ValidationError({'duracao': ['duracao < 60 minutos']})
  
  STATUS_ENUM = (
       ('pago', 'Paga'),
       ('pendente', 'Pendente'),
       ('cancelado', 'Cancelada'),
  )

  TIPO_ENUM = (
       ('SAIBRO', 'Saibro'),
       ('HARD', 'Hard'),
  )
  
  tipo = models.CharField(max_length=32, choices=TIPO_ENUM)
  valor = models.PositiveIntegerField(default=0)
  status = models.CharField(max_length=32, choices=STATUS_ENUM, default='pendente')
  duracao = models.PositiveIntegerField(default=0)
  criadoEm = models.DateTimeField(auto_now_add=True)
  inicioEm = models.DateTimeField(null=True, blank=True, validators=[_valida_hora_quebrada])
  fimEm = models.DateTimeField(null=True, blank=True, validators=[_valida_hora_quebrada])
  canceladoEm = models.DateTimeField(null=True, blank=True)

  def save(self, *args, **kwargs):
    self.duracao = (self.fimEm - self.inicioEm).seconds/60
    self._periodo_minimo(self.duracao)
    self.valor = self.duracao * 0.5
    super(Reserva, self).save(*args, **kwargs)

  def delete(self):
    self.status = 'cancelado'
    self.canceladoEm = datetime.now(tz=timezone.utc)
    self.save()

  def __str__(self):
    return self.tipo + "," + self.status + "," + self.inicioEm.isoformat() + "," + self.fimEm.isoformat()+ "," + self.canceladoEm.isoformat()
