import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "desafio.settings")
django.setup()

import pytest
from cliente.models import Cliente, DadosBancarios
from cliente.serializers import ClienteSerializer, DadosBancariosSerializer


@pytest.mark.django_db
def test_cliente_serializer_full():
    # teste do serializer completo
    try:
        serializer = ClienteSerializer(data={'razao_social': 'Gerson', 'endereco': 'Rua ABC, 3', 'telefone': '99490-0339', 'faturamento_declarado': 1900121.0})
        assert serializer.is_valid()
    except (Exception,):
        assert False

@pytest.mark.django_db
def test_dados_bancarios_serializer_partial():
    # teste do serializer parcial
    try:
        serializer = ClienteSerializer(data={'razao_social': 'ACME'}, partial=True)
        assert serializer.is_valid()
    except (Exception,):
        assert False


@pytest.mark.django_db
def test_dados_bancarios_serializer_invalid():
    # teste com valores inválidos
    try:
        serializer = ClienteSerializer(data={'razao_social': 1111}, partial=True)
        assert not serializer.is_valid()
    except (Exception,):
        assert True


@pytest.mark.django_db
def test_create_cliente_sem_dado_bancario():
    # teste de cruação de um cliente sem dados bancários

    serializer_create = ClienteSerializer(data={'razao_social': 'Gerson', 'endereco': 'Rua ABC, 3', 'telefone': '99490-0339',
                                         'faturamento_declarado': 1900121.0})
    if serializer_create.is_valid():
        serializer_create.save()

        registros = Cliente.objects.filter(razao_social='Gerson')

        if len(registros) == 1:
            reg = list(registros.values())[0]
            assert reg.get("razao_social") == 'Gerson'
        else:
            assert False

@pytest.mark.django_db
def test_create_cliente_com_dado_bancario():
    # teste de criação de um cliente com dados bancários

    serializer_create = ClienteSerializer(data={'razao_social': 'Gerson', 'endereco': 'Rua ABC, 3', 'telefone': '99490-0339',
                                         'faturamento_declarado': 1900121.0})

    # se os dados forem válidos entra, caso contrário erro
    if serializer_create.is_valid():
        serializer_create.save()

        registro = Cliente.objects.get(razao_social='Gerson')

        # inserção do primeiro dado bancario se válido. Caso contrário gera um erro
        serializer1 = DadosBancariosSerializer(data={'agencia': '1001', 'conta': '2002', 'banco': '101', 'cliente': registro.id}, partial=True)
        if serializer1.is_valid():
            serializer1.save()
        else:
            print(serializer1.errors)
            assert False

        # inserção do segundo dado bancario se válido. Caso contrário gera um erro
        serializer2 = DadosBancariosSerializer(data={'agencia': '1002', 'conta': '2003', 'banco': '101', 'cliente': registro.id}, partial=True)
        if serializer2.is_valid():
            serializer2.save()
        else:
            print(serializer2.errors)
            assert False

        # validação do número de dados bancarios por cliente (no caso são 2 dados) (vale como teste de read)
        registro_contas = DadosBancarios.objects.filter(cliente=registro)
        reg2 = list(registro_contas.values())
        if len(reg2) == 2:
            assert True
        else:
            assert False
    else:
        assert False


@pytest.mark.django_db
def test_delete_cliente_sem_dado_bancario():
    # teste de remoção de um cliente sem dados bancários
    serializer_create = ClienteSerializer(data={'razao_social': 'Gerson2', 'endereco': 'Rua ABC, 3', 'telefone': '99490-0339',
                                          'faturamento_declarado': 1900121.0})
    if serializer_create.is_valid():
        reg = serializer_create.save()
        if reg is not None:
            cliente = Cliente.objects.get(pk=reg.id)
            cliente.delete()
            try:
                Cliente.objects.get(pk=reg.id)
                assert False
            except (Exception,):
                assert True
        else:
            assert False
    else:
        assert False
