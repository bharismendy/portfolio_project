from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from utilisateur.forms.LoginForm import LoginForm
from utilisateur.forms.SignUpForm import SignUpForm
from common.lib.context import context_general


def auth(request):
    """
    controler that allow the user to login or register on the web site
    :param request: request variable
    :return: a view with both form (login and register)
    """
    error_login = False
    error_register = False
    if request.method == 'POST' and 'btn-login' in request.POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            identifiant = login_form.cleaned_data["identifiant"]
            password = login_form.cleaned_data["mot_de_passe"]
            user = authenticate(username=identifiant, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'administration
                return redirect(reverse('accueil'))
            else:  # sinon une erreur sera affichée
                error_login = True
    else:
        login_form = LoginForm()

    if request.method == 'POST' and 'btn-register' in request.POST:
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return redirect(reverse('accueil'))

    else:
        register_form = SignUpForm()

    context = {'register_form': register_form, 'login_form': login_form, 'error_login': error_login,
               'error_register': error_register}
    context.update(context_general())

    return render(request, "utilisateur/auth.html", context)
