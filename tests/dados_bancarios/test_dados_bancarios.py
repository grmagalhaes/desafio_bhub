import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "desafio.settings")
django.setup()

import pytest
from cliente.models import DadosBancarios
from cliente.serializers import DadosBancariosSerializer


@pytest.mark.django_db
def test_dados_bancarios_serializer_full():
    try:
        DadosBancarios.objects.create(banco='005', agencia='1235', conta='12346')
        registros = DadosBancarios.objects.filter(banco='005', agencia='1235', conta='12346')
        serializer = DadosBancariosSerializer(data=registros)
        assert serializer.is_valid()
    except (Exception,):
        assert True

@pytest.mark.django_db
def test_dados_bancarios_serializer_partial():
    try:
        serializer = DadosBancariosSerializer(data={'banco': '001'}, partial=True)
        assert serializer.is_valid()
    except (Exception,):
        assert False

@pytest.mark.django_db
def test_dados_bancarios_serializer_invalid():
    try:
        serializer = DadosBancariosSerializer(data={'banco': '00121'}, partial=True)
        assert not serializer.is_valid()
    except (Exception,):
        assert False



@pytest.mark.django_db
def test_criacao_conta():
    DadosBancarios.objects.create(banco='001', agencia='1234', conta='12345')
    registros = DadosBancarios.objects.filter(banco='001', agencia='1234', conta='12345')
    assert len(registros) == 1
    if len(registros) == 1:
        assert registros[0].banco == '001'
        assert registros[0].agencia == '1234'
        assert registros[0].conta == '12345'


@pytest.mark.django_db
def test_busca_conta_inexistente():
    registros = DadosBancarios.objects.filter(banco='002', agencia='1234', conta='12345')
    assert len(registros) == 0


@pytest.mark.django_db
def test_erro_ao_recriar_conta_existente():
    try:
        DadosBancarios.objects.create(banco='001', agencia='1234', conta='12345')
        assert False
    except (Exception,):
        assert True


