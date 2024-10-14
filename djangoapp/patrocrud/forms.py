from django import forms
from .models import ModeloVeiculo, Montadora


class ModeloVeiculoForm(forms.ModelForm):
    class Meta:
        model = ModeloVeiculo
        fields = [
            "nome",
            "montadora",
            "valor_referencia",
            "motorizacao",
            "turbo",
            "automatico",
        ]
        widgets = {
            "montadora": forms.Select(attrs={"class": "form-control"}),
            "valor_referencia": forms.NumberInput(attrs={"class": "form-control"}),
            "motorizacao": forms.NumberInput(attrs={"class": "form-control"}),
            "turbo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "automatico": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

class MontadoraForm(forms.ModelForm):
    class Meta:
        model = Montadora
        fields = ["nome", "pais", "ano_fundacao"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "pais": forms.TextInput(attrs={"class": "form-control"}),
            "ano_fundacao": forms.NumberInput(attrs={"class": "form-control"}),
        }
