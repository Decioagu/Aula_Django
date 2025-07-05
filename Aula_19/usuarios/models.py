from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager

# 18 Gerenciador de usuário (autenticação e autorização)
class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    # Método auxiliar para criar um usuário
    def _create_user(self, email, password, **extra_fields):
        # e-mal é obrigatório
        if not email: 
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Métodos para criar usuários
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        # extra_fields.setdefault('is_staff', True)
        return self._create_user(email, password, **extra_fields)

    # Método para criar um superusuário
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True) #18 Superusuário precisa ter is_superuser=True
        extra_fields.setdefault('is_staff', True) #18  usuário tem permissão de login no admin

        #18 Verifica se é superusuário
        if extra_fields.get('is_superuser') is not True: 
            raise ValueError('Superuser precisa ter is_superuser=True')

        #18 Verifica se tem permissão de login no admin
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)

#18 Modelagem de usuário customizando (Criar)
class CustomUsuario(AbstractUser):
    email = models.EmailField('E-mail', unique=True) # E-mail é obrigatório e único
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'email' # Campo de login (e-mail)
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone'] # Campos obrigatórios para criação de usuário

    def __str__(self):
        return self.email

    objects = UsuarioManager() # Usando o gerenciador de usuário customizado



