from django.shortcuts import render
from django.http import HttpResponseRedirect
from portfolio.forms.LoginForm import LoginForm
from portfolio.forms.SignUpForm import SignUpForm
from django.contrib.auth import authenticate, login


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
            email = login_form.cleaned_data["email"]
            password = login_form.cleaned_data["password"]
            user = authenticate(email=email, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return HttpResponseRedirect('dashboard/history')
            else:  # sinon une erreur sera affichée
                error_login = True
    else:
        login_form = LoginForm()

    if request.method == 'POST' and 'btn-register' in request.POST:
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            return HttpResponseRedirect('accueil')

    else:
        register_form = SignUpForm()

    return render(request, 'portfolio/log_in_out.html', {'register_form': register_form,
                                                         'login_form': login_form,
                                                         'error_login': error_login,
                                                         'error_register': error_register})

