import uuid
from django.test import TestCase
from model_bakery import baker

from core.models import get_file_path

#16 Teste automatizado de imagem do Banco de Dados
class GetFilePathTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        # Verifica se o caminho do arquivo gerado tem o tamanho correto
        self.assertTrue(len(arquivo), len(self.filename)) 

#16 Teste automatizado de Serviço de Banco de Dados
class ServicoTestCase(TestCase):

    def setUp(self):
        self.servico = baker.make('Servico')

    def test_str(self):
        # Verifica se o método __str__ retorna o nome do serviço
        self.assertEqual(str(self.servico), self.servico.servico) 

#16 Teste automatizado de Cargo de Banco de Dados
class CargoTestCase(TestCase):

    def setUp(self):
        self.cargo = baker.make('Cargo')

    def test_str(self):
        # Verifica se o método __str__ retorna o nome do cargo
        self.assertEqual(str(self.cargo), self.cargo.cargo) 

#16 Teste automatizado de Equipe de Banco de Dados
class EquipeTestCase(TestCase):

    def setUp(self):
        self.equipe = baker.make('Equipe')

    def test_str(self):
        # Verifica se o método __str__ retorna o nome da equipe
        self.assertEqual(str(self.equipe), self.equipe.nome) 

