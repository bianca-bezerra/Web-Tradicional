from django.db import models
from django_ulid.models import default, ULIDField


class Montadora(models.Model):
    id = ULIDField(default=default, primary_key=True, editable=False)
    nome = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ano_fundacao = models.IntegerField()

    def __str__(self):
        return self.nome


class ModeloVeiculo(models.Model):
    id = ULIDField(default=default, primary_key=True, editable=False)
    nome = models.CharField(max_length=100)
    montadora = models.ForeignKey(
        Montadora, on_delete=models.CASCADE, related_name="modelos"
    )
    valor_referencia = models.DecimalField(max_digits=10, decimal_places=2)
    motorizacao = models.DecimalField(max_digits=5, decimal_places=2)
    turbo = models.BooleanField(default=False)
    automatico = models.BooleanField(default=False)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    id = ULIDField(default=default, primary_key=True, editable=False)
    modelo = models.ForeignKey(
        ModeloVeiculo, on_delete=models.CASCADE, related_name="veiculos"
    )
    cor = models.CharField(max_length=50)
    ano_fabricacao = models.IntegerField()
    ano_modelo = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    placa = models.CharField(max_length=7, unique=True)
    vendido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.modelo.nome} - {self.placa}"
