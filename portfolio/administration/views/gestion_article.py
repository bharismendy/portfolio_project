from django.shortcuts import render, redirect
from article.models import Article
from common.lib.context import context_general


def gestion_art(request):
    list_article = Article.objects.all().order_by('id')
    context = {'list_article': list_article}
    context.update(context_general())
    return render(request, 'administration/gestion_article.html', context)


def switch_publish(request, id_article):
    article_to_switch = Article.objects.get(id=id_article)
    if request.POST:
        article_to_switch.publish = request.POST.get('publish')
        article_to_switch.save()
    return redirect('administration/gestion_article')
