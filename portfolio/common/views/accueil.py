from django.shortcuts import render


def accueil(request):
    return render(request=request, template_name='common/accueil.html')
