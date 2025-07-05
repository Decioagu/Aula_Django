from django.db import models
from django.contrib.auth import get_user_model

#20 Tabela de Chassi
class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo de 16 caracteres')

    #20 Definindo nome na descrição do serviço Django Admin (nome de apresentação)
    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.numero

#20 Tabela de Montadora
class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)

    #20 Definindo nome na descrição do serviço Django Admin (nome de apresentação)
    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome

#20 Função para definir uma montadora padrão caso não exista
def set_default_montadora():
    return Montadora.objects.get_or_create(nome='Padrão')[0] # (objeto, boolean)
'''
Montadora.objects.get_or_create(nome='Padrão')[0]

Busca uma montadora com o nome 'Padrão'. 
Se não encontrar, cria uma nova montadora com o nome "Padrão".

    - Montadora = Classe Montadora.
    - .objects = Método que retorna um gerenciador de objetos para a classe Montadora.
    - .get_or_create = Método que tenta obter um objeto com os parâmetros fornecidos.
    - [0] = Retorna uma tupla (objeto, boolean), Exemplo: (<Montadora: Padrão>, True/False)

OBS: [0] na tupla o valor boolean é sempre descartado retornando somente o valor do objeto.
Resultado: independentemente do resultado True/False, retorno sempre o valor "Padrão"

'''

class Carro(models.Model):
    """
    # OneToOneField (Um para Um)
    Cada carro só pode se relacionar com um chassi
    e cada chassi só pode se relacionar com um carro.

    # ForeignKey (Um para Muitos)
    Cada carro tem uma montadora mas uma montadora
    pode 'montar' vários carros.

    # ManyToMany (Muitos para Muitos)
    Um carro pode ser dirigido por vários motoristas
    e um motorista pode dirigir diversos carros.
    """
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE) #20 Um carro tem um chassi único
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora)) #20 Um carro pertence a uma montadora, se a montadora for excluída, o carro será associado à montadora "Padrão" | outra opção seria colocar valor padrão Montadora como default='Padrão' ou null=True
    motoristas = models.ManyToManyField(get_user_model()) #20 Um carro pode ser dirigido por vários motoristas
    modelo = models.CharField('Modelo', max_length=30, help_text='Máximo de 30 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    '''
        "get_user_model()": é uma boa prática quando você está trabalhando com o modelo de usuário
        customizado, personalizado ou até mesmo o modelo padrão do Django (User). Ela retorna 
        o modelo de usuário cadastrados no seu projeto (Django Admin).
    '''

    #20 Definindo nome na descrição do serviço Django Admin (nome de apresentação)
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    #20 Retorna o nome da montadora e o modelo do carro
    def __str__(self):
        return f'{self.montadora} {self.modelo}' 
