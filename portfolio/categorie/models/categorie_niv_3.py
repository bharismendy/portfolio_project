from django.db import models


class CategorieNiv3(models.Model):
    """this class is use to categorise every article"""
    nom_categorie = models.CharField(max_length=100, default=None, null=False)