from article.models import Article
from django.shortcuts import render
from common.lib.context import context_general


def affichage_article(request, id_article):
    article = Article.objects.get(id=id_article)
    context = {'article': article}
    context.update(context_general())
    return render(request, 'articles/affichage_article.html', context)
