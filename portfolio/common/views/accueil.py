from django.shortcuts import render
from article.models import Article
from common.lib.context import context_general
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def accueil(request):
    """
    view to display the root template
    :param request:environement variable
    :return: template of the root page
    """
    list_of_article = Article.objects.all().order_by('id')
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
    return render(request, 'common/accueil.html', context)
