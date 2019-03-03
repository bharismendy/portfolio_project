from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.account, name='account'),
    path('auth/', views.auth, name='auth')
]