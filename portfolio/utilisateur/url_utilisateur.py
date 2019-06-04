from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.account, name='utilisateur/dashboard'),
    path('auth/', views.auth, name='auth'),
    path('deconnexion/', views.deconnexion, name='utilisateur/deconnexion')
]