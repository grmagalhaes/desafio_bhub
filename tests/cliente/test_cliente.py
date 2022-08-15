import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "desafio.settings")
django.setup()

import pytest
from cliente.models import Cliente


@pytest.mark.django_db
def test_criacao_cliente():
    Cliente.objects.create(razao_social='Teste123', telefone='1234', endereco='rua 123', faturamento_declarado=1000)
    registros = Cliente.objects.filter(razao_social='Teste123')
    assert len(registros) == 1
    if len(registros) == 1:
        assert registros[0].razao_social == 'Teste123'

