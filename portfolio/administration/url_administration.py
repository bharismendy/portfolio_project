from django.urls import path
from . import views

urlpatterns = [
    path('gestion_categorie/', views.gestion_cat, name='administration/gestion_categorie'),
    path('admin_panel/', views.admin_panel, name='administration/admin_panel'),
]