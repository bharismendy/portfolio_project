from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.account, name='utilisateur/dashboard'),
    path('admin_panel/', views.admin_panel, name='administration/admin_panel'),
    path('auth/', views.auth, name='auth')
]