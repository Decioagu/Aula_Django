from django.test import TestCase # Importa a classe TestCase para testes automatizados
from django.test import Client # Importa a classe TestCase para testes automatizados
from django.urls import reverse_lazy # Importa a função reverse_lazy para redirecionamento

#16 Teste automatizado de View de Index
class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Felicity Jones',
            'email': 'felicity@gmail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha mensagem'
        }

        # Cria um cliente de teste para simular requisições HTTP
        self.cliente = Client() 

    # envia os dados do formulário para a view 'index'
    def test_form_valid(self):
        # Envia os dados do formulário para a view 'index'
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        # Redireciona para a página de sucesso
        self.assertEqual(request.status_code, 302) 

    # envia dados inválidos para a view 'index'
    def test_form_invalid(self):
        dados = {
            'nome': 'Felicity Jones',
            'assunto': 'Meu assunto'
        }
        # Envia dados inválidos para a view 'index'
        request = self.cliente.post(reverse_lazy('index'), data=dados)
        # Verifica se o status code é 200 (OK) para dados inválidos
        self.assertEqual(request.status_code, 200) 