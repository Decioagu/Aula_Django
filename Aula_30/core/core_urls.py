from django.urls import path

from core.views import index_list_view


urlpatterns = [
    path('', index_list_view, name='index'), # http://localhost:8000
]
