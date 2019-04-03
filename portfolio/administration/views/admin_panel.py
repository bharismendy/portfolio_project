from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from common.lib.context import context_general


@login_required
def admin_panel(request):
    context = context_general()
    return render(request, 'administration/admin_panel.html', context)
