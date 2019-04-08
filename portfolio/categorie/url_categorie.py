from django.urls import path
from . import views

urlpatterns = [
    path('new_cat_1/', views.new_cat_un, name='categorie/new_cat_1'),
    path('new_cat_2/', views.new_cat_deux, name='categorie/new_cat_2'),
    path('new_cat_3/', views.new_cat_trois, name='categorie/new_cat_3'),
    path('new_cat_4/', views.new_cat_quatre, name='categorie/new_cat_4'),
]
