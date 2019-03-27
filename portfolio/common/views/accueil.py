from django.shortcuts import render
from article.models import Article
from common.lib.context import context_general


def accueil(request):
    list_of_article = Article.objects.all().order_by('id')
    return render(request, 'common/accueil.html', {'articles': list_of_article}.update(context_general()))


