from django.db import models
from categorie.models import CategorieNiv3


class CategorieNiv4(models.Model):
    """this class is use to categorise every article"""
    nom_categorie = models.CharField(max_length=100, default=None, null=False)
    cat_sup = models.ForeignKey(CategorieNiv3, on_delete=models.CASCADE, default=None, null=False)

    def __str__(self):
        return self.nom_categorie
