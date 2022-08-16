from rest_framework import serializers
from .models import Cliente, DadosBancarios


class DadosBancariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = DadosBancarios
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
