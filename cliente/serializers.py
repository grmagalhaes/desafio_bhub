from rest_framework import serializers
from .models import Cliente, DadosBancarios


class DadosBancariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosBancarios
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    contas = DadosBancariosSerializer(many=True, read_only=True)

    class Meta:
        model = Cliente
        fields = ['id', 'razao_social', 'telefone', 'endereco', 'data_cadastro', 'faturamento_declarado', 'contas']
        depth = 1
