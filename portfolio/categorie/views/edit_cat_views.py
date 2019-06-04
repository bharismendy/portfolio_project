from categorie.forms import CategorieForm
from django.shortcuts import render, redirect
from django.urls import reverse
from common.lib.context import context_general
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from categorie.models import Categorie


@login_required
def edit_cat(request, id_cat):
    """
    create a new category of level 1
    :param request: environement variable
    :param id_cat: id of the category
    :return: template with a form
    """
    if not request.user.is_superuser:  # security to redirect user that aren't admin
        return redirect(reverse('accueil'))

    category = get_object_or_404(Categorie, id=id_cat)
    form_cat = CategorieForm(request.POST or None, instance=category)
    if form_cat.is_valid():
        form_cat.save()
        return redirect(reverse('administration/gestion_categorie'))
    context = {'form_cat': form_cat, 'id_cat': id_cat}
    context.update(context_general())
    return render(request, 'administration/edit_of_categorie.html', context)
