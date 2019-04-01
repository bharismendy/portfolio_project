from django.urls import path
from . import views

urlpatterns = [
    path('new_article/', views.new_article, name='article/new_article'),
    path('affichage_article/<int:id_article>', views.affichage_article, name='article/affichage'),
    path('edition_article/<int:id_article>', views.edit_article, name='article/edition')
]
