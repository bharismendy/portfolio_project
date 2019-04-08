from article.forms import EditArticle
from django.shortcuts import render, redirect
from django.urls import reverse
from common.lib.context import context_general
from django.contrib.auth.decorators import login_required


@login_required
def new_article(request):
    """
    view to create a new article
    :param request: environement variable containing POST, FILES and GET values
    :return: a template to the form article with errors or the root of the website
    """
    if request.method == "POST":
        form_article = EditArticle(request.POST, request.FILES)
        if form_article.is_valid():
            form_article.save(user=request.user.personne)
            return redirect(reverse('accueil'))
    else:
        form_article = EditArticle()

    context = {'form_article': form_article}
    context.update(context_general())
    return render(request, 'articles/article_new.html', context)

