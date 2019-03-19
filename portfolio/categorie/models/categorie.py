from django.db import models


class Categorie(models.Model):
    """this class is use to categorise every article"""
    nom_categorie = models.CharField(default=None, null=False)
