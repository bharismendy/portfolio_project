from django.shortcuts import render
from article.forms import EditArticle


def new_article(request):
    form_article = EditArticle()
    return render(request, 'articles/article_edit.html', {'form_article': form_article})
