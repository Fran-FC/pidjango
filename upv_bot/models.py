from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class GymBro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=8)
    clau = models.CharField(max_length=32)


class Reserva(models.Model):
    dia_ejecucion = models.DateField()
    hora_ejecucion = models.TimeField()
    repetir = models.BooleanField()


    class Campus(models.TextChoices):
        ALCOY = 'alcoy', _('Alcoy')
        VALENCIA = 'valencia', _('Valencia')
    
    campus = models.CharField(
        max_length=8,
        choices=Campus.choices,
        default=Campus.VALENCIA
    ) 

class HoraReserva(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    class DiaSemana(models.TextChoices):
        LUNES = 'L', _('Lunes')
        MARTES = 'M', _('Martes')
        MIERCOLES = 'X', _('Miercoles')
        JUEVES = 'J', _('Jueves')
        VIERNES = 'V', _('Viernes')

    class HoraDelDia(models.TextChoices):
        HORA_1  = '0',  _("7:30-8:30")
        HORA_2  = '1',  _("8:30-9:30")
        HORA_3  = '2',  _("9:30-10:30")
        HORA_4  = '3',  _("11:30-12:30")
        HORA_5  = '4',  _("12:30-13:30")
        HORA_6  = '5',  _("13:30-14:30")
        HORA_7  = '6',  _("14:30-15:30")
        HORA_8  = '7',  _("15:30-16:30")
        HORA_9  = '8',  _("16:30-17:30")
        HORA_10 = '9',  _("17:30-18:30")
        HORA_11 = '10', _("18:30-19:30")
        HORA_12 = '11', _("19:30-20:30")
        HORA_13 = '12', _("20:30-21:30")
        HORA_14 = '13', _("21:30-22:30")

    dia_reserva = models.CharField(
        max_length=1, 
        choices=DiaSemana.choices,
        default=DiaSemana.LUNES
    )

    hora_reserva = models.CharField(
        max_length=2,
        choices=HoraDelDia.choices,
        default=HoraDelDia.HORA_1
    )
    

