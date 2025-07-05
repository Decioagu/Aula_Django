from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo

'''
    "get_user_model()": é uma boa prática quando você está trabalhando com o modelo de usuário
    customizado, personalizado ou até mesmo o modelo padrão do Django (User). Ela retorna 
    o modelo de usuário cadastrados no seu projeto (Django Admin). Seja o modelo padrão do Django (User)
    ou um modelo personalizado que você tenha definido.

    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)

    Essa linha cria um relacionamento de chave estrangeira (ForeignKey) entre o modelo Post 
    e o modelo de usuário ativo no sistema (que representa o autor do post).

    - get_user_model(): retorna o modelo de usuário em uso.

    - verbose_name='Autor': serve para definir um nome legível e amigável que 
    será exibido no painel administrativo (Django Admin).

    - on_delete=models.CASCADE: indica que, se o usuário for excluído, os posts dele também serão.
'''