from django.shortcuts import redirect
from django.contrib.auth import logout


def deconnexion(request):
    """view to disconnect the user"""
    try:
        logout(request)
    except Exception as error:
        print(error)
    return redirect('accueil')
