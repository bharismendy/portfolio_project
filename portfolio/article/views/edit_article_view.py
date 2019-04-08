from article.forms import EditArticle
from django.shortcuts import render, redirect
from django.urls import reverse
from article.models import Article
from common.lib.context import context_general
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def edit_article(request, id_article):
    """
    view of a form to edit an article
    :param request: environement variable which contain GET and POST data
    :param id_article: id of the article to edit
    :return: return a template with list of all category and an article if found
    """
    try:
        art = get_object_or_404(Article, id=id_article)
    except():
        redirect('accueil')
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

