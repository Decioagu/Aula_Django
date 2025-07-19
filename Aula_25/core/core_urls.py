from django.urls import path

from core.views import IndexView, Index2View


urlpatterns = [
    path('', IndexView.as_view(), name='index'), # http://localhost:8000
    path('2/', Index2View.as_view(), name='index2'), # http://localhost:8000
]

