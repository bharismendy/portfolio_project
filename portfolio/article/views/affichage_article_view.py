from article.models import Article
from django.shortcuts import render, redirect
from common.lib.context import context_general
from django.shortcuts import get_object_or_404


def affichage_article(request, id_article):
    """
    view of an article
    :param request: environement variable which contain GET and POST data
    :param id_article: id of the article to display
    :return: return a template with list of all category and an article if found
    """
    try:
        article = get_object_or_404(Article, id=id_article)
    except():
        redirect('accueil')
    context = {'article': article}
    context.update(context_general())
    return render(request, 'articles/affichage_article.html', context)
