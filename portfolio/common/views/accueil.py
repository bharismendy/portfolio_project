from django.shortcuts import render
from article.models import Article
from common.lib.context import context_general


def accueil(request):
    list_of_article = Article.objects.all().order_by('id')
    context = {'articles': list_of_article}
    context.update(context_general())
    return render(request, 'common/accueil.html', context)


