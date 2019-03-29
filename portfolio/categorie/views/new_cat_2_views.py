from categorie.forms import NewCategorieNiv2
from django.shortcuts import render, redirect
from django.urls import reverse
from common.lib.context import context_general


def new_cat_deux(request):
    form_ncn_2 = NewCategorieNiv2(request.POST or None)
    if form_ncn_2.is_valid():
        form_ncn_2.save()
        return redirect(reverse('accueil'))
    context = {'form_cat_niv_1': form_ncn_2}
    context.update(context_general())
    return render(request, 'administration/gestion_categorie.html', context)
