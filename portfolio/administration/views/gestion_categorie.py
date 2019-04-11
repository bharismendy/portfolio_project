from django.urls import reverse
from django.shortcuts import render, redirect
from categorie.forms import CategorieForm
from categorie.models import Categorie
from common.lib.context import context_general
from django.contrib.auth.decorators import login_required


@login_required
def gestion_cat(request):
    """
    view used to create new category
    :param request: environement variable which contains POST and GET values
    :return: template with 3 forms and list of all categorie
    """
    if not request.user.is_superuser:  # security to redirect user that aren't admin
        return redirect(reverse('accueil'))
    form_cat = CategorieForm

    cat = Categorie.objects.all().order_by('niv_cat')
    niv_haut = Categorie.objects.all().order_by('niv_cat')[0].niv_cat
    niv_bas = Categorie.objects.all().order_by('-niv_cat')[0].niv_cat

    list_of_all_category = []
    for niv in range(niv_haut, niv_bas + 1):
        temp = []
        for element in cat:
            if element.niv_cat == niv:
                temp.append(element)
        list_of_all_category.insert(niv, temp[:])
        temp.clear()

    context = {'form_cat': form_cat,
               "category": list_of_all_category}

    context.update(context_general())
    return render(request, 'administration/gestion_categorie.html', context)
