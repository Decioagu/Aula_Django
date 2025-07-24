from django.urls import path, include
from django.contrib.auth import views as auth_views

from core.views import IndexView, LoginView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'), # http://localhost:8000/login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # http://localhost:8000/logout
    path('social-auth/', include('social_django.urls', namespace='social')), # http://localhost:8000/social-auth
    path('', IndexView.as_view(), name='index'), # http://localhost:8000
]
