from django.test import TestCase

from core.forms import ContatoForm

# 16 Teste automatizado de Formulário de Contato
class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Felicity Jones'
        self.email = 'felicity@gmail.com'
        self.assunto = 'Um assunto qualquer'
        self.mensagem = 'Uma mensagem qualquer'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

        # Cria uma instância do formulário ContatoForm com os dados fornecidos
        self.form = ContatoForm(data=self.dados) 
    
    # 16 Teste automatizado de Validação de Formulário de Contato
    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        res2 = form2.send_mail()

        # Verifica se o envio do e-mail é o mesmo para ambos os formulários
        self.assertEqual(res1, res2) 
