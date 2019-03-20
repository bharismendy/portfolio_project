from article.models import Article
from django.shortcuts import render


def affichage_article(request, id_article):
    article = Article.objects.get(id=id_article)
    return render(request, 'articles/affichage_article.html', {'article': article})
