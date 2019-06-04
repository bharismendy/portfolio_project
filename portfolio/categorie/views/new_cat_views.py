from categorie.forms import CategorieForm
from django.shortcuts import render, redirect
from django.urls import reverse
from common.lib.context import context_general
from django.contrib.auth.decorators import login_required


@login_required
def new_cat(request):
    """
    create a new category of level 1
    :param request: environement variable
    :return: template with a form
    """
    form_cat = CategorieForm(request.POST or None)
    if form_cat.is_valid():
        form_cat.save()
        return redirect(reverse('administration/gestion_categorie'))
    context = {'form_cat': form_cat}
    context.update(context_general())
    return render(request, 'administration/gestion_categorie.html', context)
