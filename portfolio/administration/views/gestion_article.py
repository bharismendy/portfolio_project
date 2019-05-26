from django.urls import reverse
from django.shortcuts import render, redirect
from article.models import Article
from common.lib.context import context_general
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def gestion_art(request):
    """
    view wich list all article
    :param request: environement variable which contain POST and GET
    :return: template with categorie list and list of all article paginate
    """
    if not request.user.is_superuser:  # security to redirect user that aren't admin
        return redirect(reverse('accueil'))

    list_of_article = Article.objects.all().order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(list_of_article, 9)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    context = {'list_article': articles}
    context.update(context_general())
    return render(request, 'administration/gestion_article.html', context)


@login_required
def switch_publish(request, id_article):
    """
    main view used to switch an article from public to private
    :param request: environement variable which contain POST and GET
    :param id_article: id of article to switch
    :return: redirect user to the page wich called this view
    """
    if not request.user.is_superuser:  # security to redirect user that aren't admin
        return redirect(reverse('accueil'))
    article_to_switch = Article.objects.get(id=id_article)
    if request.POST:
        article_to_switch.publish = request.POST.get('publish')
        article_to_switch.save()
    return redirect('administration/gestion_article')
