from django.shortcuts import render
from common.lib.context import context_general


def mentions(request):
    """used to show legal right for the user"""
    context = context_general()
    return render(request, 'common/mentions.html', context)
