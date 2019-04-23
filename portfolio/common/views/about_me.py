from django.shortcuts import render
from common.lib.context import context_general
from utilisateur.models import Personne


def about_me(request):
    """
    view to display information about the owner
    :param request:environement variable
    :return: template of the root page
    """
    brice = Personne.objects.filter(user__username='bharismendy')
    context = {'creator': brice}
    context.update(context_general())
    return render(request, 'common/about_me.html', context)

