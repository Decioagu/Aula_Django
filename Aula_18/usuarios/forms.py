from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from usuarios.models import CustomUsuario

#18 Formulários customizado (Criação de usuários)
class CustomUsuarioCreateForm(UserCreationForm):

    # Campo do formulário
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')
        labels = {'username': 'Username/E-mail'}

    # Método para salvar o usuário
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]
        if commit:
            user.save()
        return user

#18 Formulário customizado (Alteração de usuários)
class CustomUsuarioChangeForm(UserChangeForm):
    # Campo do formulário
    class Meta:
        model = CustomUsuario
        fields = ('first_name', 'last_name', 'fone')

