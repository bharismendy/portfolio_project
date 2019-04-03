from django.urls import path
from . import views

urlpatterns = [
    path('new_article/', views.new_article, name='article/new_article'),
    path('affichage_article/<int:id_article>', views.affichage_article, name='article/affichage'),
    path('edition_article/<int:id_article>', views.edit_article, name='article/edition'),
    path('list_by_cat/<int:niv_cat>/<int:id_cat>', views.query_cat, name='article/list_by_cat'),
    path('search', views.query_art, name='article/search')
]
