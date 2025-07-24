from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin #27 Autenticação


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'


class LoginView(TemplateView):
    template_name = 'login.html'

