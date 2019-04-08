from categorie.forms import NewCategorieNiv4
from django.shortcuts import render, redirect
from django.urls import reverse
from common.lib.context import context_general
from django.contrib.auth.decorators import login_required


@login_required
def new_cat_quatre(request):
    """
    create a new category of level 4
    :param request: environement variable
    :return: template with a form
    """
    form_ncn_4 = NewCategorieNiv4(request.POST or None)
    if form_ncn_4.is_valid():
        form_ncn_4.save()
        return redirect(reverse('accueil'))
    context = {'form_cat_niv_4': form_ncn_4}
    context.update(context_general())
    return render(request, 'administration/gestion_categorie.html', context)
