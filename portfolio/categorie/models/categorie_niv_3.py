from django.db import models
from categorie.models import CategorieNiv2


class CategorieNiv3(models.Model):
    """this class is use to categorise every article"""
    nom_categorie = models.CharField(max_length=100, default=None, null=False)
    cat_sup = models.ForeignKey(CategorieNiv2, on_delete=models.CASCADE, default=None, null=False)
