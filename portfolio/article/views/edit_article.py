from article.forms import EditArticle
from django.shortcuts import render, redirect
from django.urls import reverse


def new_article(request):

    if request.method == "POST":
        form_article = EditArticle(request.POST)
        if form_article.is_valid():
            form_article.save(user=request.user.personne)
            return redirect(reverse('accueil'))
    else:
        form_article = EditArticle()
    return render(request, 'articles/article_edit.html', {'form_article': form_article})
