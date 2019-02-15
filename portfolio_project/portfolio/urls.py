from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('accueil', views.accueil, name='accueil'),
    path('view', views.view, name='view'),
    path('auth', views.auth, name='auth'),
    path('sign_out', views.deconnexion, name='sign_out')
]
