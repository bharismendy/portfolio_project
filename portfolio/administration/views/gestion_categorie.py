from django.shortcuts import render
from categorie.forms import NewCategorieNiv1, NewCategorieNiv2, NewCategorieNiv3
from common.lib.context import context_general


def gestion_cat(request):
    form_ncn_1 = NewCategorieNiv1(request.POST or None)
    form_ncn_2 = NewCategorieNiv2(request.POST or None)
    form_ncn_3 = NewCategorieNiv3(request.POST or None)
    context = {'form_cat_niv_1': form_ncn_1,
               'form_cat_niv_2': form_ncn_2,
               'form_cat_niv_3': form_ncn_3}
    context.update(context_general())
    return render(request, 'administration/gestion_categorie.html', context)
