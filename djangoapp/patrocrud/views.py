from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .forms import ModeloVeiculoForm, MontadoraForm, VeiculoForm
from .models import ModeloVeiculo, Montadora, Veiculo
from .views_utils import create, update


def home(request):
    return render(request, "index.html")


# MONTADORA


def montadora_list(request):
    montadoras = Montadora.objects.all()
    context = {"montadoras": montadoras}
    return render(request, "montadoras/montadora_list.html", context=context)


@csrf_protect
def montadora_create(request):
    return create(
        request,
        MontadoraForm,
        "montadoras/montadora_form.html",
        "montadora_list",
        "Adicionar montadora",
    )


@csrf_protect
def montadora_delete(request, pk):
    montadora = get_object_or_404(Montadora, pk=pk)
    montadora.delete()
    messages.success(request, "Montadora deletada com sucesso.")
    return HttpResponseRedirect(reverse("montadora_list"))


def montadora_detail(request, pk):
    montadora = get_object_or_404(Montadora, pk=pk)
    return render(request, "montadoras/montadora_detail.html", {"montadora": montadora})


@csrf_protect
def montadora_update(request, pk):
    return update(
        request,
        Montadora,
        MontadoraForm,
        pk,
        "montadoras/montadora_form.html",
        "montadora_detail",
        "Editar montadora",
    )


# MODELO


def modelo_list(request):
    modelos = ModeloVeiculo.objects.all()
    return render(request, "modelos/modelo_list.html", {"modelos": modelos})


@csrf_protect
def modelo_create(request):
    return create(
        request,
        ModeloVeiculoForm,
        "modelos/modelo_form.html",
        "modelo_list",
        "Adicionar modelo",
    )


@csrf_protect
def modelo_delete(request, pk):
    modelo = get_object_or_404(ModeloVeiculo, pk=pk)
    modelo.delete()
    messages.success(request, "Modelo deletado com sucesso.")
    return HttpResponseRedirect(reverse("modelo_list"))


def modelo_detail(request, pk):
    modelo = get_object_or_404(ModeloVeiculo, pk=pk)
    return render(request, "modelos/modelo_detail.html", {"modelo": modelo})


@csrf_protect
def modelo_update(request, pk):
    return update(
        request,
        ModeloVeiculo,
        ModeloVeiculoForm,
        pk,
        "modelos/modelo_form.html",
        "modelo_detail",
        "Editar modelo",
    )


# VEICULO


def veiculo_list(request):
    veiculos = Veiculo.objects.all()
    return render(request, "veiculos/veiculo_list.html", {"veiculos": veiculos})


@csrf_protect
def veiculo_create(request):
    return create(
        request,
        VeiculoForm,
        "veiculos/veiculo_form.html",
        "veiculo_list",
        "Adicionar veículo",
    )

@csrf_protect
def veiculo_delete(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    veiculo.delete()
    messages.success(request, "Veiculo deletado com sucesso.")
    return HttpResponseRedirect(reverse("veiculo_list"))


def veiculo_detail(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    return render(request, "veiculos/veiculo_detail.html", {"veiculo": veiculo})


@csrf_protect
def veiculo_update(request, pk):
    return update(
        request,
        Veiculo,
        VeiculoForm,
        pk,
        "veiculos/veiculo_form.html",
        "veiculo_detail",
        "Editar veículo",
    )
