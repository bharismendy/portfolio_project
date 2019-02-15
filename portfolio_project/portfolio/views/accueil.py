from django.shortcuts import render
from portfolio.models.categorie_article import CategorieNiv3, CategorieNiv2, CategorieNiv1


def accueil(request):
    """
    controler of the template accueil.html
    :param request: variable wich contains the value of the page
    :return: template html
    """
    categorie_niveau_1 = CategorieNiv1.objects.all()
    categorie_niveau_2 = CategorieNiv2.objects.all()
    categorie_niveau_3 = CategorieNiv3.objects.all()

    return render(request, 'portfolio/accueil.html', {
        'cat_1': categorie_niveau_1,
        'cat_2': categorie_niveau_2,
        'cat_3': categorie_niveau_3,
    })
