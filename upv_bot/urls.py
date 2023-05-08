from django.urls import include, path

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path("", views.index, name="index"),
    path("inicio_reserva", views.inicio_reserva, name="inicio_reserva"),
]
