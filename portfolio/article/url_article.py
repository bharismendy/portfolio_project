from django.urls import path
from . import views

urlpatterns = [
    path('new_article/', views.new_article, name='article/new_article')
]