from datetime import datetime

from django.db import models

# Modelos utilizados no Desafio BHub
# Cliente e seus Dados Bancários


class Cliente(models.Model):
    razao_social = models.CharField(max_length=60, blank=False)
    telefone = models.CharField(max_length=14, null=True)
    endereco = models.CharField(max_length=60, blank=False)
    data_cadastro = models.DateTimeField(default=datetime.now(), null=False)
    faturamento_declarado = models.DecimalField(max_digits=12, decimal_places=2, null=True)

    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['razao_social'], name='cliente_unique')
        ]

    def __str__(self):
        return f"{self.razao_social}"


class DadosBancarios(models.Model):
    banco = models.CharField(max_length=3, blank=False)
    agencia = models.CharField(max_length=6, blank=False)
    conta = models.CharField(max_length=12, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)

    objects = models.Manager()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['banco', 'agencia', 'conta'], name='dados_bancarios_unique')
        ]

    def __str__(self):
        return f"{self.banco} | {self.agencia} | {self.conta}"
