from django.db import models
from categorie.models import CategorieNiv1


class CategorieNiv2(models.Model):
    """this class is use to categorise every article"""
    nom_categorie = models.CharField(max_length=100, default=None, null=False)
    cat_sup = models.ForeignKey(CategorieNiv1, on_delete=models.CASCADE, default=None, null=False)

