from article.forms import EditArticle
from django.shortcuts import render, redirect
from django.urls import reverse
from common.lib.context import context_general


def new_article(request):
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

