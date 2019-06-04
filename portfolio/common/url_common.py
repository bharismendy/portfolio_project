from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('accueil', views.accueil, name='accueil'),
    path('mention', views.mentions, name='mention'),
    path('about_me', views.about_me, name='about_me')
]