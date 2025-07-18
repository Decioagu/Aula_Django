from django.urls import path

from core.views import IndexView, DadosJSONView


urlpatterns = [
    path('', IndexView.as_view(), name='index'), # http://localhost:8000
    path('dados/', DadosJSONView.as_view(), name='dados'), # http://localhost:8000/dados
]
