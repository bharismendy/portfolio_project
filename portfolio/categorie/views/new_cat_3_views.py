from categorie.forms import NewCategorieNiv3
from django.shortcuts import render, redirect
from django.urls import reverse
from common.lib.context import context_general
from django.contrib.auth.decorators import login_required


@login_required
def new_cat_trois(request):
    """
    create a new category of level 3
    :param request: environement variable
    :return: template with a form
    """
    form_ncn_3 = NewCategorieNiv3(request.POST or None)
    if form_ncn_3.is_valid():
        form_ncn_3.save()
        return redirect(reverse('accueil'))
    context = {'form_cat_niv_3': form_ncn_3}
    context.update(context_general())
    return render(request, 'administration/gestion_categorie.html', context)
