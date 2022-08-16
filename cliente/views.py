from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status

from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from cliente.utils import hardening_header
from .models import Cliente, DadosBancarios
from .serializers import ClienteSerializer, DadosBancariosSerializer

from .messages import ClienteMessages as Msg


class ClientViewSet(ViewSet):
    authentication_classes = []

    # cria um cliente sem contas vinculadas
    def create(self, request):
        try:
            serializer = ClienteSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                cliente = serializer.save()
                return Response(data=dict(msg=Msg.CLIENTE_CADASTRADO_SUCESSO, id=cliente.id),
                                status=status.HTTP_200_OK, headers=hardening_header())
            else:
                return Response(data=dict(msg=Msg.ERRO_CADASTRO_CLIENTE, id=None),
                                status=status.HTTP_400_BAD_REQUEST, headers=hardening_header())

        except (IntegrityError,) as e:
            return Response(data=dict(msg=Msg.CLIENTE_JA_CADASTRADO, id=None),
                            status=status.HTTP_400_BAD_REQUEST, headers=hardening_header())
        except (Exception,) as e:
            return Response(data=dict(msg=Msg.ERRO_CADASTRO_CLIENTE, id=None),
                            status=status.HTTP_400_BAD_REQUEST, headers=hardening_header())

    # retorna um cliente e todas as suas contas
    def get(self, request):
        client_id = request.query_params.get('id')
        clientes = Cliente.objects.filter(pk=client_id).values()

        if len(clientes) > 0:
            serializer = ClienteSerializer(data=clientes[0], partial=True)

            contas = list(DadosBancarios.objects.filter(cliente=client_id).values())

            if serializer.is_valid():
                serializer.validated_data['contas'] = contas
                return Response(data=serializer.validated_data, headers=hardening_header())
            else:
                return Response(data=dict(msg=Msg.ERRO_CADASTRO_CLIENTE, id=None),
                                status=status.HTTP_400_BAD_REQUEST, headers=hardening_header())
        else:
            return Response(data=dict(msg=Msg.CLIENTE_NAO_ENCONTRADO, id=None),
                            status=status.HTTP_404_NOT_FOUND, headers=hardening_header())

    # atualiza um cliente
    def update(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(data=serializer.data, headers=hardening_header())

    # atualiza um cliente
    def list(self, request):
        clientes = Cliente.objects.all().values()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(data=serializer.data, headers=hardening_header())

    # remove um cliente e todas as contas vinculadas a ele
    def delete(self, request):
        client_id = request.query_params.get('id')
        try:
            cliente = Cliente.objects.get(pk=client_id)
            if cliente is not None:
                cliente.delete()
                return Response(status=status.HTTP_204_NO_CONTENT, headers=hardening_header())
            else:
                return Response(data=dict(msg=Msg.CLIENTE_NAO_ENCONTRADO, id=None),
                                status=status.HTTP_404_NOT_FOUND, headers=hardening_header())
        except (ObjectDoesNotExist,):
            return Response(data=dict(msg=Msg.CLIENTE_NAO_ENCONTRADO, id=None),
                            status=status.HTTP_404_NOT_FOUND, headers=hardening_header())


class DadosBancariosViewSet(ViewSet):

    def add_account(self, request):
        dados_bancarios = DadosBancariosSerializer(data=request.data, partial=True)
        if dados_bancarios.is_valid():
            try:
                dados_bancarios.save()
                return Response(data=dict(msg=Msg.CONTA_CADASTRADA_SUCESSO),
                                status=status.HTTP_200_OK, headers=hardening_header())
            except (IntegrityError,) as e:
                print (str(e))
                return Response(data=dict(msg=Msg.CONTA_JA_CADASTRADA),
                                status=status.HTTP_400_BAD_REQUEST, headers=hardening_header())
        else:
            return Response(data=dict(msg=Msg.ERRO_CADASTRO_CONTA),
                            status=status.HTTP_400_BAD_REQUEST, headers=hardening_header())

    def remove_account(self, request):
        conta_id = request.query_params.get('id')
        try:
            conta = DadosBancarios.objects.get(pk=conta_id)
            if conta is not None:
                conta.delete()
                return Response(status=status.HTTP_204_NO_CONTENT, headers=hardening_header())
            else:
                return Response(data=dict(msg=Msg.CONTA_NAO_ENCONTRADA),
                                status=status.HTTP_404_NOT_FOUND, headers=hardening_header())
        except (ObjectDoesNotExist,):
            return Response(data=dict(msg=Msg.CONTA_NAO_ENCONTRADA),
                            status=status.HTTP_404_NOT_FOUND, headers=hardening_header())

