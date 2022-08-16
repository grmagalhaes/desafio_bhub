from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status

from django.db.utils import IntegrityError

from cliente.utils import hardening_header

from .models import Cliente, DadosBancarios
from .serializers import ClienteSerializer, DadosBancariosSerializer

from .messages import CLIENTE_CADASTRADO_SUCESSO, CLIENTE_JA_CADASTRADO, ERRO_CADASTRO_CLIENTE


class ClientViewSet(ViewSet):
    authentication_classes = []

    def create(self, request):
        try:
            serializer = ClienteSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                cliente = serializer.save()
                return Response(data=dict(msg=CLIENTE_CADASTRADO_SUCESSO, id=cliente.id),
                                status=status.HTTP_200_OK, headers=hardening_header())
            else:
                return Response(data=dict(msg=ERRO_CADASTRO_CLIENTE, id=None),
                                status=status.HTTP_400_BAD_REQUEST, headers=hardening_header())

        except (IntegrityError,) as e:
            return Response(data=dict(msg=CLIENTE_JA_CADASTRADO, id=None),
                            status=status.HTTP_400_BAD_REQUEST, headers=hardening_header())
        except (Exception,) as e:
            return Response(data=dict(msg='Erro de Cadastro de Cliente', id=None),
                            status=status.HTTP_400_BAD_REQUEST, headers=hardening_header())



    def read(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(data=serializer.data, headers=hardening_header())

    def update(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(data=serializer.data, headers=hardening_header())

    def delete(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(data=serializer.data, headers=hardening_header())

    def list(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(data=serializer.data, headers=hardening_header())


class DadosBancariosViewSet(ViewSet):

    def add_account(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(data=serializer.data, headers=hardening_header())

    def remove_account(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(data=serializer.data, headers=hardening_header())




