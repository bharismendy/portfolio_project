from article.forms import EditArticle
from django.shortcuts import render, redirect
from django.urls import reverse
from article.models import Article


def edit_article(request,id_article):
    if request.method == "POST":
        form_article = EditArticle(request.POST, request.FILES)
        if form_article.is_valid():
            form_article.save(user=request.user.personne)
            return redirect(reverse('accueil'))
    else:
        art = Article.objects.get(id=id_article)
        form_article = EditArticle(article=art)
    return render(request, 'articles/article_edit.html', {'form_article': form_article})

