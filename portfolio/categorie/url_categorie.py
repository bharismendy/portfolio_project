from django.urls import path
from . import views

urlpatterns = [
    path('new_cat/', views.new_cat, name='categorie/new_cat'),
]
