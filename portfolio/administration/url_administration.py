from django.urls import path
from . import views
from categorie.views import edit_cat

urlpatterns = [
    path('gestion_categorie/', views.gestion_cat, name='administration/gestion_categorie'),
    path('edition_categorie/<int:id_cat>', edit_cat, name='administration/edition_categorie'),
    path('gestion_article/', views.gestion_art, name='administration/gestion_article'),
    path('gestion_article/switch_publish/<int:id_article>', views.switch_publish,
         name='administration/gestion_article/switch_publish'),
    path('admin_panel/', views.admin_panel, name='administration/admin_panel'),
]
