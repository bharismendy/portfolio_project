from django.urls import path
from . import views

urlpatterns = [
    path('gestion_categorie/', views.gestion_cat, name='administration/gestion_categorie'),
    path('gestion_article/', views.gestion_art, name='administration/gestion_article'),
    path('gestion_article/switch_publish/<int:id_article>', views.switch_publish,
         name='administration/gestion_article/switch_publish'),
    path('admin_panel/', views.admin_panel, name='administration/admin_panel'),
]