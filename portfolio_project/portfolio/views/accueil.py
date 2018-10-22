from django.shortcuts import render


def accueil(request):
    """
    controler of the template accueil.html
    :param request: variable wich contains the value of the page
    :return: template html
    """
    return render(request, 'portfolio/accueil.html')
