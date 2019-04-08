from django.urls import reverse
from django.shortcuts import render, redirect
from categorie.forms import NewCategorieNiv1, NewCategorieNiv2, NewCategorieNiv3, NewCategorieNiv4
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
    form_ncn_1 = NewCategorieNiv1(request.POST or None)
    form_ncn_2 = NewCategorieNiv2(request.POST or None)
    form_ncn_3 = NewCategorieNiv3(request.POST or None)
    form_ncn_4 = NewCategorieNiv4(request.POST or None)
    context = {'form_cat_niv_1': form_ncn_1,
               'form_cat_niv_2': form_ncn_2,
               'form_cat_niv_3': form_ncn_3,
               'form_cat_niv_4': form_ncn_4}
    context.update(context_general())
    return render(request, 'administration/gestion_categorie.html', context)

