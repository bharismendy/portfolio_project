from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from utilisateur.models import Personne
from utilisateur.forms import EditUserProfile
from article.models import Article
from common.lib.context import context_general


@login_required
def account(request):
    """
    controler of the template account that allow to edit the user profile
    :param request: variable wich contains the value of the page
    :return: template html
    """
    try:
        test = Personne.objects.get(user=request.user)  # on tente de récupérer le one to one field Personne
    except ObjectDoesNotExist:
        request.user.personne = Personne.objects.create(user=request.user)

    if request.method == 'POST' and 'btn-update-profil' in request.POST:
        form_edit_utilisateur = EditUserProfile(data=request.POST, user=request.user, files=request.FILES)
        if form_edit_utilisateur.is_valid():
            form_edit_utilisateur.save()
    else:
        form_edit_utilisateur = EditUserProfile(data=request.POST, user=request.user)

    if request.method == 'POST' and 'btn-password' in request.POST:
        form_edit_password = PasswordChangeForm(data=request.POST, user=request.user)

        if form_edit_password.is_valid():
            user = form_edit_password.save()
            update_session_auth_hash(request, user)  # Important!
    else:
        form_edit_password = PasswordChangeForm(request.user)
    # récupération de l'historique des evalutation et le karma
    list_of_article = Article.objects.filter(personne=request.user.personne)

    context = {'form_edit_utilisateur': form_edit_utilisateur, 'form_edit_password': form_edit_password,
               'list_of_article': list_of_article}
    context.update(context_general())
    return render(request, 'utilisateur/profil.html', context)
