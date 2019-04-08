from django.shortcuts import render
from common.lib.context import context_general


def about_me(request):
    """
    view to display information about the owner
    :param request:environement variable
    :return: template of the root page
    """
    context = context_general()
    return render(request, 'common/about_me.html', context)

