from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required
def deconnexion(request):
    """view to disconnect the user"""
    try:
        logout(request)
    except Exception as error:
        print(error)
    return redirect('accueil')
