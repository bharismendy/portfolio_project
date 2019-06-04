from django.shortcuts import render, redirect
from article.models import Article
from common.lib.context import context_general
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from article.forms import RechercheArt


def query_cat(request, id_cat):
    """
    views to query a category
    :param request: environement variable
    :param niv_cat: level of a category
    :param id_cat: id of the category
    :return: template listing accurate category
    """
    list_of_article = Article.objects.filter(categorie=id_cat).order_by('id')
    if len(list_of_article) == 1:
        # on redirige vers l'article directement
        return redirect('/article/affichage_article/'+str(list_of_article[0].id)+'')
    page = request.GET.get('page', 1)
    paginator = Paginator(list_of_article, 9)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {'articles': articles}
    context.update(context_general())
    return render(request, 'articles/search_categorie.html', context)


def query_art(request):
    """
    views to query a list of article
    :param request: environement variable
    :return: template listing accurate article paginate
    """
    form_search = RechercheArt(request.GET)
    search_content = request.GET.get('search_field', None)
    search_type = request.GET.get('choice_field', None)
    if search_type == "Titre":
        list_of_article = Article.objects.filter(titre__contains=search_content).order_by('date')
    elif search_type == "Resume":
        list_of_article = Article.objects.filter(resume__contains=search_content).order_by('date')
    elif search_type == "Contenu":
        list_of_article = Article.objects.filter(contenu__contains=search_content).order_by('date')
    elif search_type == "Tout":
        list_of_article = Article.objects.filter(titre__contains=search_content) | \
                          Article.objects.filter(content__contains=search_content).order_by('date') | \
                          Article.objects.filter(resume__contains=search_content).order_by('date')
        list_of_article = list_of_article.order_by('date')
    elif not search_content or not search_type:
        list_of_article = Article.objects.all().order_by('id')
    else:
        list_of_article = Article.objects.all().order_by('id')

    page = request.GET.get('page', 1)
    paginator = Paginator(list_of_article, 9)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {'form_search': form_search, 'articles': articles}
    context.update(context_general())
    return render(request, 'articles/search_article.html', context)
