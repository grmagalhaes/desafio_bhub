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
        serializer = DadosBancariosSerializer(data={'banco': '005', 'agencia': '135', 'conta': '1246', 'cliente': None})
        assert serializer.is_valid()
    except (Exception,):
        assert False


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
def test_create_dado_bancario():
    serializer_create = DadosBancariosSerializer(data={'banco': '001', 'agencia': '1234', 'conta': '12345'}, partial=True)

    if serializer_create.is_valid():
        serializer_create.save()

        registros = DadosBancarios.objects.filter(banco='001', agencia='1234', conta='12345')

        if len(registros) == 1:
            reg = list(registros.values())[0]
            assert reg.get("banco") == '001'
            assert reg.get("agencia") == '1234'
            assert reg.get("conta") == '12345'
        else:
            assert False
    else:
        assert False


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

@pytest.mark.django_db
def test_delete_dado_bancario():
    serializer_create = DadosBancariosSerializer(data={'banco': '701', 'agencia': '1234', 'conta': '12345'}, partial=True)

    if serializer_create.is_valid():
        x = serializer_create.save()

        try:
            reg = DadosBancarios.objects.get(pk=x.id)
            reg.delete()
            assert True
        except (Exception,):
            assert False

        try:
            reg = DadosBancarios.objects.get(pk=x.id)
            reg.delete()
            assert False
        except (Exception,):
            assert True

