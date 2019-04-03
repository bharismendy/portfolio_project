from django.shortcuts import render
from common.lib.context import context_general


def mentions(request):
    context = context_general()
    return render(request, 'common/mentions.html', context)
