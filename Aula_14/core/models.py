import uuid
from django.db import models

from stdimage.models import StdImageField

'''
    Criação de modelo Banco de Dados para alimentação da pagina HTML
    nos conteúdos de Serviços, Cargos e Funcionários.
    Pagina: http://127.0.0.1:8000/
'''

#14 Função para gerar nome de imagem aleatório e único no Banco de Dados
def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

#14 Criando o modelo base para os outros modelos
class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True) # data de criação do registro
    modificado = models.DateField('Atualização', auto_now=True) # data de atualização do registro
    ativo = models.BooleanField('Ativo', default=True) # campo de indicação de registro ativo

    class Meta:
        abstract = True

'''
   Carregar imagem e dados da pagina HTML conteúdo de Serviços 
'''
#14 Criando o modelo Serviço que herda de Base
class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    ) # Definindo as opções de ícones disponíveis
    servico = models.CharField('Serviço', max_length=100) # nome do serviço
    descricao = models.TextField('Descrição', max_length=200) # descrição do serviço
    icone = models.CharField('Icone', max_length=12, choices=ICONE_CHOICES) # nome do ícone definido na opção acima

    #14 Definindo o nome do serviço e descrição para o admin (nome de apresentação)
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico

'''
   Carregar dados da pagina HTML conteúdo Cargos 
'''
#14 Criando o modelo Cargo que herda de Base
class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100) # nome do cargo

    #14 Definindo o nome do serviço e descrição para o admin (nome de apresentação)
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

'''
   Carregar imagem e dados da pagina HTML conteúdo de Serviços 
'''
#14 Criando o modelo Funcionario que herda de Base
class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE) # relacionamento com o modelo Cargo
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    #14 Definindo o nome do serviço e descrição para o admin (nome de apresentação)
    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome




