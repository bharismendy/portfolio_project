from categorie.forms import NewCategorieNiv3
from django.shortcuts import render, redirect
from django.urls import reverse
from common.lib.context import context_general


def new_cat_trois(request):
    form_ncn_3 = NewCategorieNiv3(request.POST or None)
    if form_ncn_3.is_valid():
        form_ncn_3.save()
        return redirect(reverse('accueil'))
    context = {'form_cat_niv_1': form_ncn_3}
    context.update(context_general())
    return render(request, 'administration/gestion_categorie.html', context)
