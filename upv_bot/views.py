from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ReservaForm

@login_required
def index(request):
    return render(request, "index.html")

@login_required
def inicio_reserva(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = InicioReservaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            
            # redirect to a new URL:
            return HttpResponseRedirect("reservar_horas")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InicioReservaForm()

    return render(request, "inicio_reserva.html", {"form": form})
