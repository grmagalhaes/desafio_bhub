from abc import ABC

from rest_framework import serializers
from .models import Cliente, DadosBancarios


class DadosBancariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosBancarios
        fields = ['banco', 'agencia', 'conta']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['razao_social', 'telefone', 'endereco', 'data_cadastro', 'faturamento_declarado', 'dados_bancarios']
