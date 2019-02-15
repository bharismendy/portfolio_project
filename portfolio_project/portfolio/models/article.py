from django.db import models
from portfolio.models.categorie_article import CategorieNiv1, CategorieNiv2, CategorieNiv3


class Article(models.Model):
    id = models.BigAutoField(primary_key=True)
    titre = models.CharField(max_length=300, null=False, default="default title")
    resume = models.CharField(max_length=300, null=True)
    content = models.TextField(null=False, default="lorem ipsum")
    CategorieNiv1 = models.ForeignKey(CategorieNiv1, on_delete=None)
    CategorieNiv2 = models.ForeignKey(CategorieNiv2, on_delete=None)
    CategorieNiv3 = models.ForeignKey(CategorieNiv3, on_delete=None)

