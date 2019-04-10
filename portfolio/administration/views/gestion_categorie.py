from django.urls import reverse
from django.shortcuts import render, redirect
from categorie.forms import CategorieForm
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
    context = {'form_cat': form_cat}

    context.update(context_general())
    return render(request, 'administration/gestion_categorie.html', context)

