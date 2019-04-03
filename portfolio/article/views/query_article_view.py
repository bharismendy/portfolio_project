from django.shortcuts import render
from article.models import Article
from common.lib.context import context_general
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from article.forms import RechercheArt


def query_cat(request, niv_cat, id_cat):
    list_of_article = None
    if niv_cat == 1:
        list_of_article = Article.objects.filter(categorie_niv1=id_cat).order_by('id')
    if niv_cat == 2:
        list_of_article = Article.objects.filter(categorie_niv2=id_cat).order_by('id')
    if niv_cat == 3:
        list_of_article = Article.objects.filter(categorie_niv3=id_cat).order_by('id')

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
    form_search = RechercheArt()
    search_content = request.GET.get('search_field', None)
    search_type = request.GET.get('choice_field', None)
    list_of_article = None
    if search_type == "titre":
        list_of_article = Article.objects.filter(titre__contains=search_content).order_by('date')
    elif search_type == "resume":
        list_of_article = Article.objects.filter(resume__contains=search_content).order_by('date')
    elif search_type == "contenu":
        list_of_article = Article.objects.filter(contenu__contains=search_content).order_by('date')
    elif search_type == "tout":
        list_of_article = Article.objects.filter(titre__contains=search_content) | \
                          Article.objects.filter(content__contains=search_content).order_by('date') | \
                          Article.objects.filter(resume__contains=search_content).order_by('date')
        list_of_article = list_of_article.order_by('date')

    else:
        pass#list_of_article = Article.objects.all().order_by('id')

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
