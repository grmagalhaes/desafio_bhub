from django.test import TestCase
from .models import Cliente, DadosBancarios


class DadosBancariosTestCase(TestCase):

    def test_criacao_dados_bancarios(self):
        DadosBancarios.objects.create(banco='001', agencia='1234', conta='12345')
        registros = DadosBancarios.objects.filter(banco='001', agencia='1234', conta='12345')
        # self.assertEquals(len(registros) == 1)
        self.assertEquals(registros[0].banco, '001')
        self.assertEquals(registros[0].agencia, '1234')
        self.assertEquals(registros[0].conta, '12345')

    #def test_criacao_cliente(self):
    #    Cliente.objects.create(nome='Teste', representante='Gerson2')
    #    loja_id = Cliente.objects.get(nome='Teste')
    #    self.assertEquals(loja_id.representante, 'Gerson2')

