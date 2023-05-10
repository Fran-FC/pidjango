from django import forms

class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class InicioReservaForm(forms.Form):
    # Inicio reserva
    dia_inicio = forms.DateField(label="Dia para empezar a reservar las sesiones", widget=DateInput)
    hora_inicio = forms.TimeField(label="Hora para empezar a reservar las sesiones", widget=TimeInput)
    repetir = forms.BooleanField(label="¿Se repite todas las semanas?")

    