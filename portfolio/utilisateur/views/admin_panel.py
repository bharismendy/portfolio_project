from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def admin_panel(request):
    return render(request, 'utilisateur/admin_panel.html')
