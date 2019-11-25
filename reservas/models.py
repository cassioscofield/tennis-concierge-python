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
  valor = models.PositiveIntegerField()
  status = models.CharField(max_length=32, choices=STATUS_ENUM, default='pendente')
  duracao = models.PositiveIntegerField(default=0)
  criadoEm = models.DateTimeField(auto_now_add=True)
  inicioEm = models.DateTimeField(null=True, blank=True)
  fimEm = models.DateTimeField(null=True, blank=True)
  canceladoEm = models.DateTimeField(null=True, blank=True)

  def save(self, *args, **kwargs):
    self.valor = 0
    self.duracao = 0
    super(Reserva, self).save(*args, **kwargs)
  def __str__(self):
    return self.tipo + self.status
