from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from common.lib.context import context_general


@login_required
def admin_panel(request):
    """
    main view of the admin panel
    :param request: environement variable which contain POST and GET
    :return: template with categorie variable
    """
    if not request.user.is_superuser:  # security to redirect user that aren't admin
        return redirect(reverse('accueil'))
    context = context_general()
    return render(request, 'administration/admin_panel.html', context)
