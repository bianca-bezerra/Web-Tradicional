from dataclasses import field
from django import forms
from .models import ModeloVeiculo, Montadora, Veiculo


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
            "nome": forms.TextInput(),
            "montadora": forms.Select(attrs={"class": "dropdown"}),
            "valor_referencia": forms.NumberInput(),
            "motorizacao": forms.NumberInput(),
            "turbo": forms.CheckboxInput(),
            "automatico": forms.CheckboxInput(),
        }

        labels = {
            "nome": "Nome",
            "montadora": "Montadora",
            "valor_referencia": "Valor de Referência",
            "motorizacao": "Motorização",
            "turbo": "Turbo",
            "automatico": "Automático",
        }


class MontadoraForm(forms.ModelForm):
    class Meta:
        model = Montadora
        fields = ["nome", "pais", "ano_fundacao"]
        widgets = {
            "nome": forms.TextInput(),
            "pais": forms.TextInput(),
            "ano_fundacao": forms.NumberInput(),
        }
        labels = {
            "nome": "Nome",
            "pais": "País",
            "ano_fundacao": "Ano de Fundação",
        }


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = [
            "modelo",
            "cor",
            "ano_fabricacao",
            "ano_modelo",
            "valor",
            "placa",
            "vendido",
        ]
        widgets = {
            "modelo": forms.Select(attrs={'class':'dropdown'}),
            "cor": forms.TextInput(),
            "ano_fabricacao": forms.NumberInput(),
            "ano_modelo": forms.NumberInput(),
            "valor": forms.NumberInput(),
            "placa": forms.TextInput(),
            "vendido": forms.CheckboxInput(),
        }
        labels = {
            "modelo": "Modelo",
            "cor": "Cor",
            "ano_fabricacao": "Ano de Fabricação",
            "ano_modelo": "Ano do Modelo",
            "valor": "Valor",
            "placa": "Placa",
            "vendido": "Vendido",
        }
