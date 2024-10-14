from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ModeloVeiculoForm, MontadoraForm
from .models import ModeloVeiculo, Montadora


# Create your views here.


def home(request):
    return render(request, "index.html")


def montadora_list(request):
    montadoras = Montadora.objects.all()
    context = {"montadoras": montadoras}
    return render(request, "montadoras/montadora_list.html", context=context)


def montadora_create(request):
    if request.method == "POST":
        form = MontadoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("montadora_list")
    else:
        form = MontadoraForm()

    return render(request, "montadoras/montadora_form.html", {"form": form})


def montadora_delete(request, pk):
    montadora = get_object_or_404(Montadora, pk=pk)
    montadora.delete()
    return HttpResponseRedirect(reverse("montadora_list"))


def montadora_detail(request, pk):
    montadora = get_object_or_404(Montadora, pk=pk)

    return render(request, "montadoras/montadora_detail.html", {"montadora": montadora})


# MODELO

def modelo_list(request):
    modelos = ModeloVeiculo.objects.all()
    return render(request, "modelos/modelo_list.html", {"modelos": modelos})


def modelo_create(request):
    if request.method == "POST":
        form = ModeloVeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("modelo_list")
    else:
        form = ModeloVeiculoForm()

    return render(request, "modelos/modelo_form.html", {"form": form})


def modelo_delete(request, pk):
    modelo = get_object_or_404(ModeloVeiculo, pk=pk)
    modelo.delete()
    return HttpResponseRedirect(reverse("modelo_list"))
