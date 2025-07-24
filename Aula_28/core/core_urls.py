from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),  # http://localhost:8000
    path('criar/', views.criar_produto, name='criar_produto'),  # http://localhost:8000/criar
    path('<int:id>/editar/', views.editar_produto, name='editar_produto'),  # http://localhost:8000/1/editar
    path('<int:id>/delete/', views.deletar_produto, name='deletar_produto'),  # http://localhost:8000/1/delete
]

