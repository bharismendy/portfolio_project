from article.forms import EditArticle
from django.shortcuts import render, redirect
from django.urls import reverse
from article.models import Article
from common.lib.context import context_general


def edit_article(request, id_article):
    art = Article.objects.get(id=id_article)
    if request.method == "POST":
        form_article = EditArticle(request.POST, request.FILES, instance=art)
        if form_article.is_valid():
            print("b")
            form_article.save(user=request.user.personne)
            return redirect(reverse('accueil'))
    else:
        form_article = EditArticle(instance=art)
    context = {'form_article': form_article, 'id_article': id_article}
    context.update(context_general())
    return render(request, 'articles/article_edit.html', context)

