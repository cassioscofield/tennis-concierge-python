from django.db import models

# Create your models here.
class Reserva(models.Model):
  
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
  valor = models.DecimalField(max_digits=7, decimal_places=2)
  status = models.CharField(max_length=32, choices=STATUS_ENUM, default='pendente')
  duracao = models.PositiveIntegerField(default=0)
  criadoEm = models.DateTimeField(auto_now_add=True)
  inicioEm = models.DateTimeField(null=True, blank=True)
  fimEm = models.DateTimeField(null=True, blank=True)
  canceladoEm = models.DateTimeField(null=True, blank=True)

  def save(self):
    super(Reserva, self).save()
  def __str__(self):
    return self.tipo + self.status
